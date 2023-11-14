from enum import Enum
from typing import List

from paginas_de_processo import PaginasProcesso


class Processo:
    def __init__(self, id_processo: int, tamanho: int, tamanho_pagina):
        self.id = id_processo
        self.tamanho = tamanho
        self.estado = Estado.NOVO
        self.operacoes: List[str] = []
        self.paginas_de_processo = PaginasProcesso()
        self.paginas_de_processo.cria_paginas(tamanho, tamanho_pagina)

    def get_paginas(self):
        return self.paginas_de_processo.paginas


class Estado(Enum):
    NOVO = 0
    PRONTO = 1
    BLOQUEADO = 2
    EXECUTANDO = 3
    FINALIZADO = 4
    PRONTO_SUSPENSO = 5
    SUSPENSO_BLOQUEADO = 6
