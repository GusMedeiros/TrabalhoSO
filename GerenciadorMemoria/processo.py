from enum import Enum
from math import ceil
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
        self.paginas_de_processo.cria_paginas(tamanho, tamanho_pagina, id_processo)

    def finalizar(self):
        self.estado = Estado.FINALIZADO
        self.tamanho = 0

    def get_paginas(self):
        return self.paginas_de_processo.paginas

    def get_num_pagina_e_offset(self, endereco_logico):
        pagina = endereco_logico // tamanho_pagina
        offset = endereco_logico % tamanho_pagina
        if not self.dentro_dos_limites(endereco_logico):
            raise Exception("Erro: Tentativa de acessar byte fora do limite")
        return {"pagina": pagina, "offset": offset}

    def checar_limites(self, endereco_logico):
        if endereco_logico < 0:
            raise Exception("Erro! Endereço negativo passado.")

        qtd_paginas = ceil(self.tamanho // tamanho_pagina)  # definicao correta
        pagina_correspondente = endereco_logico // tamanho_pagina  # definicao correta
        offset = endereco_logico % tamanho_pagina  # definicao correta
        ultima_pagina = qtd_paginas - 1  # obvio

        if pagina_correspondente > ultima_pagina:
            raise Exception("ERRO! Endereço corresponde a uma página maior do que o permitido")

        # ultima pagina pode ter espaço nao usado. esse espaço deve estar fora do limite
        espaco_nao_usado = (qtd_paginas * tamanho_pagina) - self.tamanho  # definicao correta
        ultimo_byte_permitido = tamanho_pagina - espaco_nao_usado
        if pagina_correspondente == ultima_pagina and offset > ultimo_byte_permitido:
            raise Exception("ERRO! Endereço corresponde à última página, porém cai em espaço não-ocupado da página.")


class Estado(Enum):
    NOVO = 0
    PRONTO = 1
    BLOQUEADO = 2
    EXECUTANDO = 3
    FINALIZADO = 4
    PRONTO_SUSPENSO = 5
    SUSPENSO_BLOQUEADO = 6
