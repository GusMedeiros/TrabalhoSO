from typing import List

from debug_logger import DebugLogger
from processo import Processo


class TabelaProcessos:
    def __init__(self, tamanho_pagina):
        self.tamanho_pagina = tamanho_pagina
        self.prox_id = 0  # pegar sempre pela funcao create_id para autoincrementar quando usar, pra nunca repetir
        self.processos: List[Processo] = []
        self.ids_utilizados = set()

    def cria_processo(self, tamanho, id_processo=None):
        id_processo = self.create_id(id_processo)
        self.processos.append(Processo(id_processo, tamanho, self.tamanho_pagina))
        return id_processo

    def create_id(self, id_processo):
        if id_processo and id_processo in self.ids_utilizados:
            raise Exception("Erro! O ID imposto já existe. Considere não especificar um ID.")
        elif id_processo:
            self.ids_utilizados.add(id_processo)
            return id_processo

        id_processo = self.prox_id
        while id_processo in self.ids_utilizados:
            id_processo = self.prox_id
            self.prox_id += 1
        self.ids_utilizados.add(id_processo)
        return id_processo

    def get_processos(self):
        return self.processos

    def busca_processo(self, id_processo):
        if id_processo is None:
            return None
        for processo in self.processos:
            if processo.id == id_processo:
                return processo

    def indice_processo(self, id_processo):
        for i, processo in enumerate(self.processos):
            if processo.id == id_processo:
                return i
