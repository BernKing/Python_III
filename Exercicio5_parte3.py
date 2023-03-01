
numeros = []
while True:
    num = int(input("Introduza numero positivo:"))
    if num == -1:
        break
    elif num < 0:
        print("Numero negativo. errado")
    else:
        numeros.append(num)


print("O maior e:", max(numeros), "Menor:", min(numeros))