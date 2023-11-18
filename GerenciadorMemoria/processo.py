from enum import Enum
from typing import List

from paginas_de_processo import PaginasProcesso
from config import tamanho_pagina


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
    
    def get_num_pagina_e_offset(self, endereco_logico):
        total_de_paginas = self.tamanho // tamanho_pagina
        bits_pagina = total_de_paginas.bit_length()
        bits_offset = tamanho_pagina.bit_length() - bits_pagina
        
        #Andamos o valor do offset para a direita para obter o número da página
        numero_pagina = endereco_logico >> bits_offset
        if(numero_pagina > total_de_paginas):
            print("ERRO: tentativa de acessar página fora do limite")
            return
        #Pegamos os bits_offset menos significativos como o offset
        offset = endereco_logico % pow(2, bits_offset)
        ret = {"pagina": numero_pagina, "offset": offset}
        return ret


class Estado(Enum):
    NOVO = 0
    PRONTO = 1
    BLOQUEADO = 2
    EXECUTANDO = 3
    FINALIZADO = 4
    PRONTO_SUSPENSO = 5
    SUSPENSO_BLOQUEADO = 6
