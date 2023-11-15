from typing import List

from GerenciadorMemoria.pagina import Pagina
from GerenciadorMemoria.quadro import Quadro


class Memoria:
    def __init__(self, tamanho_memoria, tamanho_quadro):
        self.indice_atual = 0
        self.lista_enderecos: List[Quadro] = []
        self._criar_quadros(tamanho_memoria, tamanho_quadro)

    def _criar_quadros(self, tamanho_memoria, tamanho_quadro):
        qtd_quadros = tamanho_memoria // tamanho_quadro
        for i in range(qtd_quadros - 1):
            self.lista_enderecos.append((Quadro(0)))

    def alocar(self, pagina: Pagina):
        inicio_busca = self.indice_atual
        i_quadro, quadro_atual = self.next()
        if not quadro_atual.ocupado:
            quadro_atual.ocupado = True
            pagina.numero_quadro = i_quadro
            return
        while i_quadro != inicio_busca:
            i_quadro, quadro_atual = self.next()
            if not quadro_atual.ocupado:
                quadro_atual.ocupado = True
                pagina.numero_quadro = i_quadro
                return


    def next(self):
        ultimo_quadro = self.lista_enderecos[self.indice_atual]
        indice_quadro = self.indice_atual
        self.indice_atual = (self.indice_atual + 1) % len(self.lista_enderecos)
        return indice_quadro, ultimo_quadro

    def checar_disponibilidade(self, qtd_paginas):
        contador = 0
        for quadro in self.lista_enderecos:
            if not quadro.ocupado:
                contador += 1
                if contador == qtd_paginas:
                    return True
        return False

    def calcular_uso(self):
        contador = 0
        for quadro in self.lista_enderecos:
            if quadro.ocupado:
                contador += 1
        return contador / len(self.lista_enderecos)

