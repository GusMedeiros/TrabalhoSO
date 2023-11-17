from typing import List

from debug_logger import DebugLogger
from pagina import Pagina
from quadro import Quadro


class Memoria:
    def __init__(self, tamanho_memoria, tamanho_quadro):
        self.proximo_indice = 0
        self.lista_enderecos: List[Quadro] = []
        self._criar_quadros(tamanho_memoria, tamanho_quadro)

    def _criar_quadros(self, tamanho_memoria, tamanho_quadro):
        qtd_quadros = tamanho_memoria // tamanho_quadro
        DebugLogger.log(
            f"Dividindo {tamanho_memoria}bytes de memória em {qtd_quadros} quadros de {tamanho_quadro}bytes.")
        for i in range(qtd_quadros):
            self.lista_enderecos.append((Quadro(tamanho_quadro)))

    def alocar(self, pagina: Pagina):
        i_quadro, quadro_atual = self.next()
        inicio_busca = i_quadro
        if not quadro_atual.ocupado:
            DebugLogger.log(f"Quadro {i_quadro} disponível. Alocando")
            quadro_atual.ocupado = True
            pagina.numero_quadro = i_quadro
            return
        DebugLogger.log(f"Quadro {i_quadro} indisponível.")
        while i_quadro != inicio_busca:
            i_quadro, quadro_atual = self.next()
            if not quadro_atual.ocupado:
                DebugLogger.log(f"Quadro {i_quadro} disponível. Alocando")
                quadro_atual.ocupado = True
                pagina.numero_quadro = i_quadro
                return
            DebugLogger.log(f"Quadro {i_quadro} indisponível.")
        DebugLogger.log("Nenhum quadro disponível encontrado.")

    def next(self):
        ultimo_quadro = self.lista_enderecos[self.proximo_indice]
        indice_quadro = self.proximo_indice
        self.proximo_indice = (self.proximo_indice + 1) % len(self.lista_enderecos)
        return indice_quadro, ultimo_quadro

    def checar_disponibilidade(self, qtd_paginas):
        contador = 0
        for quadro in self.lista_enderecos:
            if not quadro.ocupado:
                contador += 1
                if contador == qtd_paginas:
                    return True
        return False

    def qtd_quadros_ocupados(self):
        contador = 0
        for quadro in self.lista_enderecos:
            if not quadro.ocupado:
                contador += 1
        return contador

    def total_quadros(self):
        return len(self.lista_enderecos)
