from typing import List
from math import ceil

from GerenciadorMemoria.debug_logger import DebugLogger
from GerenciadorMemoria.pagina import Pagina


class PaginasProcesso:
    def __init__(self):
        self.paginas: List[Pagina] = []

    def cria_paginas(self, tamanho_processo: int, tamanho_pagina: int):
        qtd_paginas = ceil(tamanho_processo/tamanho_pagina)
        # print(tamanho_processo, tamanho_pagina, qtd_paginas)
        for i_pagina in range(qtd_paginas):
            DebugLogger.log(f"Criando página {i_pagina} na tabela de páginas do processo")
            self.paginas.append(Pagina(0))
            

