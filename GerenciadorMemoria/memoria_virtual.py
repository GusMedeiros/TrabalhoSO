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
        print(f"Página {pagina.numero} de P{pagina.id_processo} foi alocada na memoria virtual")

    def remove_pagina(self, numero_pagina, id_processo):
        for qv in self.quadros_virtuais:
            if qv.pagina.id == numero_pagina and qv.pagina.id_processo == id_processo:
                return self.quadros_virtuais.pop(qv)
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