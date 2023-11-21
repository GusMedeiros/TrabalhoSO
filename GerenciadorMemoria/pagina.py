class Pagina:
    def __init__(self, numero_quadro: int, id_pagina : int, id_processo: int):
        self.numero_quadro = numero_quadro
        self.P = False  # bit de presença na memoria principal
        self.M = False  # bit de modificação na memoria principal
        self.ciclo_ultimo_acesso = 0
        #Informação para facilitar a troca de paginas
        self.numero = id_pagina
        self.id_processo = id_processo
