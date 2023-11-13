from GerenciadorMemoria.memoria import Memoria
from tabela_processos import TabelaProcessos


class GerenciadorMemoria:

    def __init__(self, tamanho_memoria_principal, tamanho_pagina):
        self.processos = TabelaProcessos()
        self.memoria = Memoria(tamanho_memoria_principal, tamanho_pagina)

    def cria_processo(self, tamanho):
        self.processos.cria_processo(tamanho)
