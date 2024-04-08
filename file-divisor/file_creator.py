import random as ran


dados = open(
    "teste.txt", "wt")

for i in range(100):
    for j in range(1000):
        print(ran.random() * 1000)
        dados.write(str(ran.random() * 1000) + " ")
    dados.write("\n")

dados.close()


