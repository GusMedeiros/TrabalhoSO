class Quadro:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.ocupado = False
        self.bytes = bytes([0 for i in range(tamanho)])

