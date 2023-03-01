soma = 0
numeros = []
i = 0
while len(numeros) != 20:
    if i % 2 == 0:
        numeros.append(i)
    i += 1


for k in range(20):
    soma = soma + numeros[k]

print(soma)

