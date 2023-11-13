from typing import List

from pip._internal.utils.misc import enum

from paginas_de_processo import PaginasProcesso


class Processo:
    def __init__(self, id_processo: int, tamanho: int):
        self.id = id_processo
        self.tamanho = tamanho
        self.estado = Estado.NOVO
        self.operacoes: List[str] = []
        self.paginas_de_processo = PaginasProcesso()
        self.paginas_de_processo.cria_paginas(tamanho)

class Estado(enum):
    NOVO = "Novo"
    PRONTO_SUSPENSO = "Pronto Suspenso"
    PRONTO = "Pronto"
    BLOQUEADO = "Bloqueado"
    SUSPENSO_BLOQUEADO = "Suspenso Bloqueado"
    EXECUTANDO = "Executando"
    FINALIZADO = "Finalizado"
