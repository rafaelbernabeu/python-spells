import os
import argparse

parser = argparse.ArgumentParser(
    description="Divisor de arquivos por quantidade de colunas",
    usage="""$ python3 file_divisor.py exemplo.txt
       $ python3 file_divisor.py exemplo.txt -c 300 -s " "
       $ python3 file_divisor.py exemplo.txt --col 10 --separador "," """
)

parser.add_argument('nomeArquivo', type=str)
parser.add_argument('-c', '--col', type=int, help="Qtd de colunas a dividir. Default: 300", default=300)
parser.add_argument('-s', '--sep', type=str, help="Separador. Default: espaço", default=" ")

args = parser.parse_args()
numColDesejado = args.col
nomeArquivo = args.nomeArquivo
separador = args.sep

with open(nomeArquivo, "rt") as fd:
    arquivo = fd.readlines()
    qtdLinhas = len(arquivo)

nomeArquivo = nomeArquivo.split(".")[0]
qtdColunasTotal = len(arquivo[0].split(separador))
qtdArquivosCriar = int(qtdColunasTotal / numColDesejado)
resto = qtdColunasTotal % numColDesejado

if qtdColunasTotal == 1:
    print("Separador inválido")
    exit(1)

contador = 0
numArquivo = 1
saida = ""

for linha in arquivo:
    colunas = linha.split(separador)
    comprimentoOnda = colunas[0]
    ultimoItem = colunas[-1]

    for col in colunas[1::]:
        saida += col + " "
        contador += 1

        if ((contador == numColDesejado) | (col == ultimoItem)):
            try: os.mkdir(f"{os.getcwd()}/{nomeArquivo}")
            except IOError: pass
            with open(f'{os.getcwd()}/{nomeArquivo}/{nomeArquivo}_{numArquivo:03}.txt', "at") as file:
                file.write(comprimentoOnda + " " + saida.strip() + "\n")
            contador = 0
            numArquivo += 1
            saida = ""

    numArquivo = 1


print(f'Foram criados {qtdArquivosCriar} arquivos com {numColDesejado} colunas cada')
if resto > 0:
    print(f'Um arquivo com {resto} colunas restantes')