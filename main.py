import sys
import re
import lib

if __name__ == "__main__":

    args = sys.argv[1:]


    if len(args) < 3:
        print("Poucos Arqumentos...")
    else:
        chave = args[0]
        path = lib.Modo.CRIPTO if args[1] = 'C' else lib.Modo.DESCRIPTO
        modo = args[2]

        textoOriginal = open(pathEntrada, "r").read()

        # TODO: Adicionar metodo
        mensagemEmbaralhada = lib.Process(chave, textoOriginal);

        arquivoSaida = open(pathSaida, "w+")
        arquivoSaida.write(mensagemEmbaralhada)

        print("Finalizado...")