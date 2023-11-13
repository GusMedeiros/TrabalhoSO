from typing import List

from GerenciadorMemoria.quadro import Quadro


class Memoria:
    def __init__(self, tamanho_memoria, tamanho_quadro):
        self.lista_enderecos: List[Quadro] = []
        self._criar_quadros(tamanho_memoria, tamanho_quadro)

    def _criar_quadros(self, tamanho_memoria, tamanho_quadro):
        qtd_quadros = tamanho_memoria // tamanho_quadro
        for i in range(qtd_quadros):
            self.lista_enderecos[i] = Quadro(tamanho_quadro)
