nomeArquivo = "teste/teste_1.txt"

arquivo = open(nomeArquivo, "rt").readlines()
print(f"Arquivo contém {len(arquivo)} linhas")

for idx, linha in enumerate(arquivo):
    colunas = linha.strip().split(" ")
    print(f"Linha {idx} tem {len(colunas)} colunas")



