# Modulo responsavel por interpretar as intruçoes a partir de um dado arquivo

from gerenciador_memoria import GerenciadorMemoria


# P - Executa instruçao no endereço
# I - acesso de entrada e saida em disco em um dado endereço
# C - cria e submete processo com um numero dado de bytes
# W - escreve um valor no endereço de memoria
# R - Pedido de leitura
# T - termina processo

# Exemplo entrada
# "P1 R 100101001010101001010101010"

class Interpretador:
    def __init__(self, gerenciador_memoria: GerenciadorMemoria):
        self.gm = gerenciador_memoria
        self.ciclo = 0

    def executar_arquivo(self, nome_arquivo):
        with open(nome_arquivo) as instrucoes:
            for i, instrucao in enumerate(instrucoes):
                print(f"Lendo do arquivo instrução {i + 1}: {instrucao}")
                self.executar(instrucao)
                self.ciclo += 1

    def executar(self, instrucao: str):
        id_processo, tipo_instrucao, arg_3, endereco_escrita = self.parse_instrucao(instrucao)
        print("O TIPO DA INSTRUÇÃO É: ", tipo_instrucao)
        if tipo_instrucao == "P":
            self.gm.acessa_instrucao(id_processo, arg_3, self.ciclo)
            return
        if tipo_instrucao == "I":
            return
        if tipo_instrucao == "C":
            self.gm.cria_processo(arg_3, self.ciclo, id_processo)
            return
        if tipo_instrucao == "R":
            self.gm.leitura_de_memoria(id_processo, arg_3, self.ciclo)
            return
        if tipo_instrucao == "W":
            self.gm.escrita_em_memoria(id_processo, arg_3, endereco_escrita, self.ciclo)
            return
        if tipo_instrucao == "T":
            self.gm.termina_processo(id_processo, self.ciclo)
            return

    def parse_instrucao(self, instrucao):
        # P, R, W, I REQUEREM PARSE DE BINARIO
        instrucao_split = instrucao.split()
        id_processo = int(instrucao_split[0].replace("P", ""))
        tipo_instrucao = instrucao_split[1]

        if tipo_instrucao == "T":
            return id_processo, tipo_instrucao, None, None

        if tipo_instrucao in ["P", "R", "W", "I"]:
            arg_3 = int(instrucao_split[2], 2)
        else:
            arg_3 = int(instrucao_split[2])

        if tipo_instrucao != "C" and tipo_instrucao != "W":
            return id_processo, tipo_instrucao, arg_3, None
        if tipo_instrucao == "C":
            return id_processo, tipo_instrucao, self.parse_tamanho(arg_3, instrucao_split[3]), None
        endereco_escrita = int(instrucao_split[3], 2)
        return id_processo, tipo_instrucao, arg_3, endereco_escrita

    @staticmethod
    def parse_tamanho(numero_unidades: int, unidade: str):
        KB = pow(2, 10)
        MB = pow(2, 20)
        GB = pow(2, 30)
        TB = pow(2, 40)

        if unidade == "B":
            return numero_unidades
        if unidade == "KB":
            return numero_unidades * KB
        if unidade == "MB":
            return numero_unidades * MB
        if unidade == "GB":
            return numero_unidades * GB
        if unidade == "TB":
            return numero_unidades * TB
        raise (Exception("ERRO! UNIDADE MÁXIMA É TB"))
