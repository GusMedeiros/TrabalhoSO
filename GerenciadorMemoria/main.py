from GerenciadorMemoria.gerenciador_memoria import GerenciadorMemoria
from config import *


def main():
    if tamanho_memoria_principal % tamanho_pagina != 0:
        print("Erro! O tamanho da memória não é múltiplo do tamanho da página.")
    gerenciador_memoria = GerenciadorMemoria(tamanho_memoria_principal, tamanho_pagina)
    gerenciador_memoria.cria_processo(500 * pow(2, 20), 1)
    print()

main()