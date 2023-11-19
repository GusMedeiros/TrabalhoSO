from math import ceil
from typing import List
from random import randint

from debug_logger import DebugLogger
from memoria import Memoria
from pagina import Pagina
from tabela_processos import TabelaProcessos
from config import qtd_bits_endereco, tamanho_pagina

class GerenciadorMemoria:

    def __init__(self, tamanho_memoria_principal, tamanho_pagina):
        self.tamanho_pagina = tamanho_pagina
        self.tamanho_memoria_principal = tamanho_memoria_principal
        DebugLogger.log("Inicializando tabela de processos do gerenciador de memória")
        self.tabela_processos = TabelaProcessos(tamanho_pagina)
        DebugLogger.log("===Inicializando a memória principal")
        self.memoria = Memoria(tamanho_memoria_principal, tamanho_pagina)
        DebugLogger.log("===Memória principal inicializada.\n")

    def cria_processo(self, tamanho, id_processo=None):
        DebugLogger.log(f"===Criando processo de {tamanho}b")
        id_processo = self.tabela_processos.cria_processo(tamanho, id_processo)
        DebugLogger.log(f"P{id_processo} Alocado na tabela de processos no índice {self.tabela_processos.indice_processo(id_processo)}\n")
        processo = self.tabela_processos.busca_processo(id_processo)
        DebugLogger.log(f"Checando se há {tamanho}b disponíveis na MP")
        tem_espaco = self.memoria.checar_disponibilidade(self.calcula_qtd_paginas(processo.tamanho))
        if tem_espaco:
            DebugLogger.log(f"Espaço disponível. Alocando quadros na memória principal")
            self.alocar_processo(processo.get_paginas())
            DebugLogger.log(f"===Processo alocado com sucesso. Espaço utilizado: {self.calcular_uso()*100:.2f}%\n")
            return
        DebugLogger.log(f"Espaço indisponível.")

    def calcula_qtd_paginas(self, tamanho):
        return ceil(tamanho//self.tamanho_pagina)

    def alocar_processo(self, paginas: List[Pagina]):
        for i, pagina in enumerate(paginas):
            if not pagina.P:
                DebugLogger.log(f"Página {i} não presente na MP.")
                self.memoria.alocar(pagina)
                DebugLogger.log(f"Página {i} Alocada com sucesso.")
                pagina.P = True
            else:
                DebugLogger.log(f"Página {i} já está presente na MP. Prosseguindo")

    def calcular_uso(self):
        return 1 - self.memoria.qtd_quadros_ocupados()/self.memoria.total_quadros()
    
    def leitura_de_memoria(self, id_processo, endereco_logico):
        processo = self.tabela_processos.busca_processo(id_processo)
        
        pag_e_offset = processo.get_num_pagina_e_offset(endereco_logico)

        print(f"Lendo página {pag_e_offset['pagina']}, offset {pag_e_offset['offset']} de P{id_processo}")
        pagina_pedida = processo.get_paginas()[pag_e_offset['pagina']]
        if not pagina_pedida.P:
            #TODO: Trazer a pagina da memória virtual para a memória principal
            return
        quadro = self.memoria.lista_enderecos[pagina_pedida.numero_quadro]
        print(f"Valor no byte {pag_e_offset['offset']} do quadro {pagina_pedida.numero_quadro} = {quadro.bytes[pag_e_offset['offset']]}")
        return
    
    def escrita_em_memoria(self, id_processo, endereco_logico, valor):
        processo = self.tabela_processos.busca_processo(id_processo)
        
        pag_e_offset = processo.get_num_pagina_e_offset(endereco_logico)

        print(f"Acessando página {pag_e_offset['pagina']}, offset {pag_e_offset['offset']} de P{id_processo}")
        pagina_pedida = processo.get_paginas()[pag_e_offset['pagina']]
        if not pagina_pedida.P:
            #TODO: Trazer a pagina da memória virtual para a memória principal
            return
        #quando a pagina está na memória, retorna o valor no quadro correspondente
        quadro = self.memoria.lista_enderecos[pagina_pedida.numero_quadro]
        quadro.bytes[pag_e_offset["offset"]] = valor
        pagina_pedida.M = True
        print(f"Escrito o valor {valor} no offset {pag_e_offset['offset']} do quadro {pagina_pedida.numero_quadro}")
        
        return
    def acessa_instrucao(self, id_processo, endereco_logico):
        #Não está claro se a execução opera sobre outras paginas do processo
        #Nesse caso, iremos usar valores aleátorios
        processo = self.tabela_processos.busca_processo(id_processo)
        
        pag_e_offset = processo.get_num_pagina_e_offset(endereco_logico)

        print(f"Acessando intrução na página {pag_e_offset['pagina']}, offset {pag_e_offset['offset']} de P{id_processo}")
        pagina_pedida = processo.get_paginas()[pag_e_offset['pagina']]
        if not pagina_pedida.P:
            #TODO: Trazer a pagina da memória virtual para a memória principal
            return
        resultado = randint(0, 10000)
        operacao = "soma" if endereco_logico % 2 == 0 else "subtração"
        print(f"Resultado da {operacao}: {resultado}")
        return
        
