# Modulo responsavel por interpretar as intruçoes a partir de um dado arquivo

from GerenciadorMemoria import  processo
from GerenciadorMemoria.gerenciador_memoria import GerenciadorMemoria


#P - Executa instruçao no endereço
#I - acesso de entrada e saida em disco em um dado endereço
#C - cria e submete processo com um numero dado de bytes
#W - escreve um valor no endereço de memoria
#R - Pedido de leitura
#T - termina processo

# Exemplo entrada
# "P1 R 100101001010101001010101010"

class interpretador:
    def __init__(self, gerenciadorMemoria):
        self.gm = gerenciadorMemoria

    def executar(comando):
        #Separa o conteudo do comando em um array usando espaços como separador
        args = comando.split()
        #args[0] = Processo a ser executado
        #args[1] = Comando a ser executado pelo processo
        #args[2] = Argumento do comando se necessario
        print("Executando para " + args[0])
        args[0].replace("P", '')#deixa só o valor númerico como id do processo
        match args[1]:
            case "P":
                gm.acessa_instrucao(args[2])
            case "I":
                gm.acessa_disp_IO(args[2])
                # Suspende
            case "C":
                # Cria novo processo com tamanho args[2] e unidade args[3]
                # Vamos passar o valor em bytes
                tam = 0
                match args[3]:
                    case "KB":
                        tam = 1024*int(args[2])
                    case "MB":
                        tam = 1024 * 1024 * int(args[2])
                    case "GB":
                        tam = 1024 * 1024 * 1024 * int(args[2])
                    case _:
                        tam = int(args[2])

                gm.cria_processo(tam, args[0])
            case "R":
                # Pedido de leitura em args[2]
                gm.leitura_de_memoria(args[2])
            case "W":
                # Pedido de escrita de args[3] em args[2]
                gm.escrita_em_memoria(args[2], args[3])
            case "T":
                gm.termina_processo(args[0])
            case _:
                print("Comando Inválido")
        return

