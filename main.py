from GerenciadorMemoria.gerenciador_memoria import GerenciadorMemoria
from GerenciadorMemoria.memoria import Memoria


def main(
        tamanho_memoria_principal,
        tamanho_memoria_secundaria,
        tamanho_pagina,
        qtd_bits_endereco):
    if tamanho_memoria_principal % tamanho_pagina != 0:
        print("Erro! O tamanho da memória não é múltiplo do tamanho da página.")
    gerenciador_memoria = GerenciadorMemoria(tamanho_memoria_principal, tamanho_pagina)
