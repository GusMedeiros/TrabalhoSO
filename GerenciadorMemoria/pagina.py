class Pagina:
    def __init__(self, numero_quadro: int):
        self.numero_quadro = numero_quadro
        self.P = False  # bit de presença na memoria principal
        self.M = False  # bit de modificação na memoria principal
