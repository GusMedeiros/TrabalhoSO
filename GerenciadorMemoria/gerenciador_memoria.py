from math import ceil
from typing import List

from GerenciadorMemoria.debug_logger import DebugLogger
from GerenciadorMemoria.memoria import Memoria
from GerenciadorMemoria.pagina import Pagina
from tabela_processos import TabelaProcessos


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
            else:
                DebugLogger.log(f"Página {i} já está presente na MP. Prosseguindo")

    def calcular_uso(self):
        return 1 - self.memoria.qtd_quadros_ocupados()/self.memoria.total_quadros()

