from math import ceil
from typing import List

from GerenciadorMemoria.debug_logger import DebugLogger
from GerenciadorMemoria.memoria import Memoria
from GerenciadorMemoria.pagina import Pagina
from tabela_processos import TabelaProcessos


class GerenciadorMemoria:

    def __init__(self, tamanho_memoria_principal, tamanho_pagina):
        self.debug = True
        self.tamanho_pagina = tamanho_pagina
        self.tamanho_memoria_principal = tamanho_memoria_principal
        self.tabela_processos = TabelaProcessos(tamanho_pagina)
        self.memoria = Memoria(tamanho_memoria_principal, tamanho_pagina)

    def cria_processo(self, tamanho, id_processo=None):
        DebugLogger.log(f"Criando processo {id_processo} de {tamanho}b")
        self.tabela_processos.cria_processo(tamanho, id_processo)
        DebugLogger.log(f"P{id_processo} Alocado na tabela de processos no índice {self.tabela_processos.busca_processo(id_processo)}")
        processo = self.tabela_processos.busca_processo(id_processo)
        DebugLogger.log(f"Checando se há {tamanho}b disponíveis na MP")
        tem_espaco = self.memoria.checar_disponibilidade(self.calcula_qtd_paginas(processo.tamanho))
        if tem_espaco:
            DebugLogger.log(f"Espaço disponível. Alocando")
            self.alocar_processo(processo.get_paginas())

    def calcula_qtd_paginas(self, tamanho):
        return ceil(tamanho//self.tamanho_pagina)

    def alocar_processo(self, paginas: List[Pagina]):
        for pagina in paginas:
            if not pagina.P:
                self.memoria.alocar(pagina)

    def calcular_uso(self):
        return self.memoria.calcular_uso()

