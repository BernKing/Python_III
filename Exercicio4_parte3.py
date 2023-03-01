

num = []

for i in range(30):

    while True:
        numero = int(input("Introduza um numero inteiro:"))
        if numero >= 0 and int:
            num.append(numero)
            break
        print("Insira denovo")


print("O menor inserido foi:", min(num))
