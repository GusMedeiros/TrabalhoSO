# Modulo responsavel por interpretar as intruçoes a partir de um dado arquivo

from GerenciadorMemoria import  processo
from GerenciadorMemoria.processo import Processo


#P - Executa instruçao no endereço
#I - acesso de entrada e saida em disco em um dado endereço
#C - cria e submete processo com um numero dado de bytes
#W - escreve um valor no endereço de memoria
#R - Pedido de leitura
#T - termina processo

# Exemplo entrada
# "P1 R 100101001010101001010101010"

def executa(comando):
    #Separa o conteudo do comando em um array usando espaços como separador
    args = comando.split()
    #args[0] = Processo a ser executado
    #args[1] = Comando a ser executado pelo processo
    #args[2] = Argumento do comando se necessario
    print("Executando para " + args[0])
    match args[1]:
        case "P":
            # Acesso a _instruçao_ no endereço "args[2]"
            pass
        case "I":
            # Pedido de entrada e saida em um dispositivo args[2]
            # Suspende
            pass
        case "C":
            # Cria novo processo com tamanho args[2] e unidade args[3]
            args[0].replace("P", '')
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

            Processo(int(args[0]), tam)
            pass
        case "R":
            # Pedido de leitura em args[2]
            pass
        case "W":
            # Pedido de escrita em args[2]
            pass
        case "T":
            #Pedido de terminaçao do processo
            pass
        case _:
            return
    return

