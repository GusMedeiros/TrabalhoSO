from typing import List

from processo import Processo


class TabelaProcessos:
    def __init__(self, tamanho_pagina):
        self.tamanho_pagina = tamanho_pagina
        self.prox_id = 0  # pegar sempre pela funcao create_id para autoincrementar quando usar, pra nunca repetir
        self.processos: List[Processo] = []

    def cria_processo(self, tamanho, id_processo=None):
        if not id_processo:
            id_processo = self.create_id()
        self.processos.append(Processo(id_processo, tamanho, self.tamanho_pagina))

    def create_id(self):
        id_processo = self.prox_id
        self.prox_id += 1
        return id_processo

    def get_processos(self):
        return self.processos

    def busca_processo(self, id_processo):
        for processo in self.processos:
            if processo.id == id_processo:
                return processo

    def indice_processo(self, id_processo):
        for i, processo in zip(self.processos):
            if processo.id == id_processo:
                return i
