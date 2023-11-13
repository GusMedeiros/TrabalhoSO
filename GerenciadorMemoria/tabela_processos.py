from typing import List

from processo import Processo


class TabelaProcessos:
    def __init__(self):
        self.prox_id = 0  # pegar sempre pela funcao create_id para autoincrementar quando usar, pra nunca repetir
        self.processos: List[Processo] = []

    def cria_processo(self, tamanho):
        self.processos.append(Processo(self.create_id(), tamanho))

    def create_id(self):
        id_processo = self.prox_id
        self.prox_id += 1
        return id_processo
