# Exercicio 6
# Dada uma série de 20 valores reais no intervalo [0, 15], faça um programa python que
# calcule e escreva a média aritmética destes valores. Entretanto se a média obtida for
# maior que 8 deverá ser atribuída 10 para a média.


serie = []
soma = 0

for i in range(20):

    num = int(input("Insira o numero: "))
    if 0 <= num <= 15:
        serie.append(num)
    else:
        print("errado")
        i = i - 1

for k in range(20):
    soma = soma + serie[k]

media = soma // 20

if media > 8:
    media = 10
    print(media)

else:
    print(media)
