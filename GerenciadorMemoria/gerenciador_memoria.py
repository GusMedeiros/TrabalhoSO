from math import ceil
from typing import List
from random import randint

from debug_logger import DebugLogger
from memoria import Memoria
from pagina import Pagina
from tabela_processos import TabelaProcessos
from config import *
from memoria_virtual import MemoriaVirtual

class GerenciadorMemoria:

    def __init__(self, tamanho_memoria_principal, tamanho_pagina):
        self.tamanho_pagina = tamanho_pagina
        self.tamanho_memoria_principal = tamanho_memoria_principal
        DebugLogger.log("Inicializando tabela de processos do gerenciador de memória")
        self.tabela_processos = TabelaProcessos(tamanho_pagina)
        DebugLogger.log("===Inicializando a memória principal")
        self.memoria = Memoria(tamanho_memoria_principal, tamanho_pagina)
        DebugLogger.log("===Memória principal inicializada.\n")
        self.memoria_secundaria = MemoriaVirtual(tamanho_memoria_secundaria, tamanho_pagina)
        DebugLogger.log("===Memória secundária inicializada.\n")

    def cria_processo(self, tamanho, ciclo, id_processo=None):
        DebugLogger.log(f"===Criando processo de {tamanho}b")
        id_processo = self.tabela_processos.cria_processo(tamanho, id_processo)
        DebugLogger.log(f"P{id_processo} Alocado na tabela de processos no índice {self.tabela_processos.indice_processo(id_processo)}\n")
        processo = self.tabela_processos.busca_processo(id_processo)
        DebugLogger.log(f"Checando se há {tamanho}b disponíveis na MP")
        tem_espaco = self.memoria.checar_disponibilidade(self.calcula_qtd_paginas(processo.tamanho))
        if tem_espaco:
            DebugLogger.log(f"Espaço disponível. Alocando quadros na memória principal")
            self.alocar_processo(processo.get_paginas(), ciclo)
            DebugLogger.log(f"===Processo alocado com sucesso. Espaço utilizado: {self.calcular_uso()*100:.2f}%\n")
            return
        DebugLogger.log(f"Espaço indisponível. Alocando para a memoria secundaria")
        for i in processo.get_paginas():
            self.memoria_secundaria.grava_pagina(i, None)
        DebugLogger.log(f"Fim da função. Espaço utilizado: {self.calcular_uso()*100:.2f}% ")

    def calcula_qtd_paginas(self, tamanho):
        return ceil(tamanho//self.tamanho_pagina)

    def alocar_processo(self, paginas: List[Pagina], ciclo):
        for i, pagina in enumerate(paginas):
            if not pagina.P:
                DebugLogger.log(f"Página {i} não presente na MP.")
                if not self.memoria.alocar(pagina, ciclo):
                    #No caso do processo não caber totalmente na MP, alocar o restante na memória virtual
                    self.memoria_secundaria.grava_pagina(pagina, None)
                DebugLogger.log(f"Página {i} Alocada com sucesso.")
                pagina.P = True
            else:
                DebugLogger.log(f"Página {i} já está presente na MP. Prosseguindo")

    def calcular_uso(self):
        return 1 - self.memoria.qtd_quadros_ocupados()/self.memoria.total_quadros()
    
    def leitura_de_memoria(self, id_processo, endereco_logico, ciclo):
        processo = self.tabela_processos.busca_processo(id_processo)
        
        pag_e_offset = processo.get_num_pagina_e_offset(endereco_logico)

        print(f"Lendo página {pag_e_offset['pagina']}, offset {pag_e_offset['offset']} de P{id_processo}")
        pagina_pedida = processo.get_paginas()[pag_e_offset['pagina']]
        if not pagina_pedida.P:
            self.lru(pagina_pedida, ciclo)
        quadro = self.memoria.lista_enderecos[pagina_pedida.numero_quadro]
        print(f"Valor no byte {pag_e_offset['offset']} do quadro {pagina_pedida.numero_quadro} = {quadro.bytes[pag_e_offset['offset']]}")
        pagina_pedida.ciclo_ultimo_acesso = ciclo
        return
    
    def escrita_em_memoria(self, id_processo, endereco_logico, valor, ciclo):
        processo = self.tabela_processos.busca_processo(id_processo)
        
        pag_e_offset = processo.get_num_pagina_e_offset(endereco_logico)

        print(f"Acessando página {pag_e_offset['pagina']}, offset {pag_e_offset['offset']} de P{id_processo}")
        pagina_pedida = processo.get_paginas()[pag_e_offset['pagina']]
        if not pagina_pedida.P:
            self.lru(pagina_pedida, ciclo)
        #quando a pagina está na memória, retorna o valor no quadro correspondente
        quadro = self.memoria.lista_enderecos[pagina_pedida.numero_quadro]
        quadro.bytes[pag_e_offset["offset"]] = valor
        pagina_pedida.M = True
        print(f"Escrito o valor {valor} no offset {pag_e_offset['offset']} do quadro {pagina_pedida.numero_quadro}")
        pagina_pedida.ciclo_ultimo_acesso = ciclo
        return
    def acessa_instrucao(self, id_processo, endereco_logico, ciclo):
        #Não está claro se a execução opera sobre outras paginas do processo
        #Nesse caso, iremos usar valores aleátorios
        processo = self.tabela_processos.busca_processo(id_processo)
        
        pag_e_offset = processo.get_num_pagina_e_offset(endereco_logico)

        print(f"Acessando intrução na página {pag_e_offset['pagina']}, offset {pag_e_offset['offset']} de P{id_processo}")
        pagina_pedida = processo.get_paginas()[pag_e_offset['pagina']]
        if not pagina_pedida.P:
            self.lru(pagina_pedida, ciclo)
        resultado = randint(0, 10000)
        operacao = "soma" if endereco_logico % 2 == 0 else "subtração"
        print(f"Resultado da {operacao} em {pag_e_offset['pagina']}, offset {pag_e_offset['offset']} de P{id_processo}: {resultado}")
        pagina_pedida.ciclo_ultimo_acesso = ciclo
        return
    
    def acessa_disp_IO(self, id_processo, dispositivo):
        print(f"P{id_processo} está realizando uma operação de E/S no dispositivo {dispositivo}.")
        #TODO: Interrupção/suspensão de processo

    def lru(self, pagina_pedida: Pagina, ciclo):
        #Começamos da primeira página
        pagina_mais_antiga = self.tabela_processos.get_processos()[0].get_paginas()[0]

        #Procurando a pagina mais antiga
        for proc in self.tabela_processos.get_processos():
            for pag in proc.get_paginas():
                if pag.ciclo_ultimo_acesso < pagina_mais_antiga.ciclo_ultimo_acesso:
                    pagina_mais_antiga = pag
        print(f"Substituindo a página {pagina_mais_antiga.numero} de P{pagina_mais_antiga.id_processo} por {pagina_pedida.numero} de P{pagina_pedida.id_processo}.")

        #Removendo a pagina mais antiga da memória
        pagina_mais_antiga.P = False
        self.memoria_secundaria.grava_pagina(pagina_mais_antiga, self.memoria.lista_enderecos[pagina_mais_antiga.numero_quadro])
        self.memoria.desalocar(pagina_mais_antiga)
        pagina_mais_antiga.numero_quadro = None
        pagina_mais_antiga.ciclo_ultimo_acesso = None
        #Adicionando a nova pagina
        conteudo = self.memoria_secundaria.remove_pagina(pagina_pedida)    
        self.memoria.alocar(pagina_pedida, ciclo)

        if conteudo is not None and len(conteudo) > 0:
            quadro = self.memoria.lista_enderecos[pagina_pedida.numero_quadro]
            while len(conteudo) > 0:
                temp = conteudo.pop()
                quadro.bytes[temp[0]] = temp[1]
        return 