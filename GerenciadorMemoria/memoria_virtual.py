from pagina import Pagina
from config import tamanho_memoria_secundaria, tamanho_pagina
from quadro import Quadro
class MemoriaVirtual:
    def __init__(self, tamanho_memoria_secundaria, tamanho_pagina):
        self.max_paginas = tamanho_memoria_secundaria // tamanho_pagina
        self.quadros_virtuais = []
        pass
    
    def grava_pagina(self, pagina: Pagina, quadro: Quadro):
        if len(self.quadros_virtuais) >= self.max_paginas:
            print("Máximo de páginas em memoria secundária atingido!")
        self.quadros_virtuais.append(_QuadroMemoriaVirtual(quadro, pagina))
        print(f"Página {pagina.numero_quadro} de P{pagina.id_processo} foi alocada na memoria virtual")

    def remove_pagina(self, pagina_pedida):
        for i in range(len(self.quadros_virtuais)):
            if self.quadros_virtuais[i].pagina == pagina_pedida:
                qv = self.quadros_virtuais.pop(i)
                return qv.valores
        print("Pagina não encontrada!")
        return None

class _QuadroMemoriaVirtual:
    def __init__(self, quadro: Quadro, pagina: Pagina):
        self.valores = self._grava_quadro(quadro)
        self.pagina = pagina
    def _grava_quadro(self, quadro):
        valores = []
        if quadro is not None:
            for i in range(quadro.tamanho):
                if quadro.bytes[i] != 0:
                    #(Valor do offset, conteudo do byte)
                    valores.append((i, quadro.bytes[i]))
        return valores