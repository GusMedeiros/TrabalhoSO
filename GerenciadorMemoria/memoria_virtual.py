from pagina import Pagina
from config import tamanho_memoria_secundaria, tamanho_pagina
from quadro import Quadro
class MemoriaVirtual:
    def __init__(self, tamanho_memoria_secundaria, tamanho_pagina):
        self.max_paginas = tamanho_memoria_secundaria // tamanho_memoria_secundaria
        self.dict_paginas = {}
        pass
    
    def grava_pagina(self, pagina: Pagina, quadro: Quadro):
        if len(self.dict_paginas) >= self.max_paginas:
            print("Máximo de páginas em memoria secundária atingido!")
        valores = []
        if Quadro is not None:
            for i in range(quadro.tamanho):
                if quadro.bytes[i] != 0:
                    #(Valor do offset, conteudo do byte)
                    valores.append((i, quadro.bytes[i]))

        self.dict_paginas.update(pagina, valores)

    def remove_pagina(self, numero_pagina, id_processo):
        for pag in self.dict_paginas.keys:
            if pag.numero == numero_pagina and pag.id_processo == id_processo:
                return self.dict_paginas.pop(pag)
        print("Pagina não encontrada!")
        return None