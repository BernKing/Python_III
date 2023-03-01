i = 0
notas = []
while i <= 60:
    notass = int(input("Notas:"))
    if notass == -1:
        break

    notas.append(notass)
    i += 1

print(sum(notas) / len(notas))













