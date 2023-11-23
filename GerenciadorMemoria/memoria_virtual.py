from math import ceil

from pagina import Pagina
from quadro import Quadro
class MemoriaVirtual:
    def __init__(self, tamanho_memoria_secundaria, tamanho_pagina):
        self.total_quadros = ceil(tamanho_memoria_secundaria / tamanho_pagina)
        self.quadros_virtuais = []
        pass
    
    def grava_pagina(self, pagina: Pagina, quadro: Quadro):
        if len(self.quadros_virtuais) >= self.total_quadros:
            print("Máximo de páginas em memoria secundária atingido!")
            return

        self.quadros_virtuais.append(_QuadroMemoriaVirtual(quadro, pagina))
        print(f"Página {pagina.id_pagina} de P{pagina.id_processo} foi alocada na memoria virtual")

    def remove_pagina(self, pagina_pedida):
        for i in range(len(self.quadros_virtuais)):
            pag = self.quadros_virtuais[i].pagina
            if pag.id_pagina == pagina_pedida.id_pagina and pag.id_processo == pagina_pedida.id_processo:
                qv = self.quadros_virtuais.pop(i)
                return qv.valores
        print(f"Página {pagina_pedida.id_pagina} de P{pagina_pedida.id_processo}não está presente na memória virtual")
        return None

    def qtd_quadros_ocupados(self):
        return len(self.quadros_virtuais)

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