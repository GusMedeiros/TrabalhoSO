from typing import List
from math import ceil
from GerenciadorMemoria.pagina import Pagina


class PaginasProcesso:
    def __init__(self):
        self.paginas: List[Pagina] = []

    def cria_paginas(self, tamanho_processo: int, tamanho_pagina: int):
        qtd_paginas = ceil(tamanho_processo/tamanho_pagina)
        print(tamanho_processo, tamanho_pagina, qtd_paginas)
        for i_pagina in range(qtd_paginas):
            self.paginas.append(Pagina(i_pagina))
            

