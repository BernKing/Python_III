# Exercicio 3
# Elabore um programa python que permita encontrar o maior de um conjunto de números
# gerados aleatoriamente. A geração deve terminar quando for gerado um múltiplo de 7.
# Apresente o maior número e quantos números foram gerados.
import random

gerados = []


while True:
    num = random.randint(0,100)
    if num % 7 == 0:
        print(len(gerados))
        print(max(gerados))
        break
    else:
        gerados.append(num)

