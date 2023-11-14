from typing import List

from GerenciadorMemoria.pagina import Pagina
from GerenciadorMemoria.quadro import Quadro


class Memoria:
    def __init__(self, tamanho_memoria, tamanho_quadro):
        self.ultimo_endereco = 0
        self.lista_enderecos: List[Quadro] = []
        self._criar_quadros(tamanho_memoria, tamanho_quadro)

    def _criar_quadros(self, tamanho_memoria, tamanho_quadro):
        qtd_quadros = tamanho_memoria // tamanho_quadro
        for i in range(qtd_quadros - 1):
            self.lista_enderecos.append((Quadro(0)))

    def alocar(self, pagina: Pagina):
        pass

    def next(self):
        self.ultimo_endereco = (self.ultimo_endereco + 1) % len(self.lista_enderecos)
        ultimo_quadro = self.lista_enderecos[self.ultimo_endereco]
        return ultimo_quadro

    def checar_disponibilidade(self, qtd_paginas):
        contador = 0
        for quadro in self.lista_enderecos:
            if not quadro.ocupado:
                contador += 1
                if contador == qtd_paginas:
                    return True
        return False
