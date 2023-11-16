from GerenciadorMemoria.debug_logger import DebugLogger
from GerenciadorMemoria.gerenciador_memoria import GerenciadorMemoria
from config import *


def main():
    print(f"Tamanho memória principal: {tamanho_memoria_principal}b | Tamanho da página: {tamanho_pagina}b\n")
    print("Inicializando a memória. Isso pode demorar")
    if tamanho_memoria_principal % tamanho_pagina != 0:
        raise Exception("Erro! O tamanho da memória não é múltiplo do tamanho da página.")
    gerenciador_memoria = GerenciadorMemoria(tamanho_memoria_principal, tamanho_pagina)
    gerenciador_memoria.cria_processo(3 * pow(2, 20), 1)
    gerenciador_memoria.cria_processo(3 * pow(2, 20))
    gerenciador_memoria.cria_processo(3 * pow(2, 20))
    gerenciador_memoria.cria_processo(3 * pow(2, 20))
    gerenciador_memoria.cria_processo(3 * pow(2, 20))
    gerenciador_memoria.cria_processo(3 * pow(2, 20))


    input("Main finalizada. Aperte qualquer botão para sair")


DebugLogger.ligar()
main()
