from debug_logger import DebugLogger
from gerenciador_memoria import GerenciadorMemoria
from config import *
from interpretador import Interpretador


def main():
    #TODO: INSTRUCOES DE ESCRITA TEM QUE MODIFICAR BIT M
    #TODO: TRATAR QUANDO NÃO HOUVER ESPAÇO NEM NA MP NEM NA MEM SECUNDARIA
    print(f"Tamanho memória principal: {tamanho_memoria_principal}b | Tamanho da página: {tamanho_pagina}b\n")
    print("Inicializando a memória. Isso pode demorar")
    if tamanho_memoria_principal % tamanho_pagina != 0:
        raise Exception("Erro! O tamanho da memória não é múltiplo do tamanho da página.")
    gerenciador_memoria = GerenciadorMemoria(tamanho_memoria_principal, tamanho_pagina)
    ciclo = 0
    interpretador = Interpretador(gerenciador_memoria)
    interpretador.executar_arquivo("instrucoes.txt")
    input("Main finalizada. Aperte qualquer botão para sair")

DebugLogger.ligar()
main()