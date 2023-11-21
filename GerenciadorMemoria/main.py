from debug_logger import DebugLogger
from gerenciador_memoria import GerenciadorMemoria
from config import *


def main():
    print(f"Tamanho memória principal: {tamanho_memoria_principal}b | Tamanho da página: {tamanho_pagina}b\n")
    print("Inicializando a memória. Isso pode demorar")
    if tamanho_memoria_principal % tamanho_pagina != 0:
        raise Exception("Erro! O tamanho da memória não é múltiplo do tamanho da página.")
    gerenciador_memoria = GerenciadorMemoria(tamanho_memoria_principal, tamanho_pagina)
    ciclo = 0
    #TODO: Leitura de arquivo usando o interpretador
    gerenciador_memoria.cria_processo(3 * pow(2, 20), ciclo, 1)
    ciclo+=1
    gerenciador_memoria.cria_processo(3 * pow(2, 20), ciclo)
    ciclo+=1
    gerenciador_memoria.cria_processo(3 * pow(2, 20), ciclo)
    ciclo+=1
    gerenciador_memoria.cria_processo(3 * pow(2, 20), ciclo)
    ciclo+=1
    gerenciador_memoria.cria_processo(3 * pow(2, 20), ciclo)
    ciclo+=1
    gerenciador_memoria.cria_processo(3 * pow(2, 20), ciclo)
    ciclo+=1

    gerenciador_memoria.leitura_de_memoria(1, 0b1011001111110111100000, ciclo)
    ciclo+=1
    gerenciador_memoria.escrita_em_memoria(1, 0b1011001111110111100000, 10, ciclo)
    ciclo+=1
    gerenciador_memoria.leitura_de_memoria(1, 0b1011001111110111100000, ciclo)
    ciclo+=1
    gerenciador_memoria.acessa_instrucao(1, 0b0111001111110111100000, ciclo)
    ciclo+=1
    gerenciador_memoria.cria_processo(3 * pow(2, 20), ciclo)
    ciclo+=1
    input("Main finalizada. Aperte qualquer botão para sair")
    ciclo = 0


DebugLogger.ligar()
main()
