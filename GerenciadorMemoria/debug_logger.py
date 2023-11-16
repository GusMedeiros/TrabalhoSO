class DebugLogger:
    debug_ligado = False

    @classmethod
    def log(cls, string):
        if not cls.debug_ligado:
            return
        print(string)

    @classmethod
    def ligar(cls):
        cls.debug_ligado = True

    @classmethod
    def desligar(cls):
        cls.debug_ligado = False
