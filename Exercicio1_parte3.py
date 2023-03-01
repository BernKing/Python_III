#Exercicio1

# Elabore um programa python que simule uma aplicação que registe a pescaria de um
# barco de pesca. O barco, nos seus porões, pode carregar, no máximo, 150 Toneladas. A
# cada pescaria deve ser registado o valor pescado e somado ao pescado anteriormente.
# Quando atingir ou ultrapassar o valor máximo, a aplicação de terminar e o utilizador deve
# ser informado se tem, ou não, de deitar peixe ao mar e, em caso afirmativo, que
# quantidade.
pescado_total = 0

while True:

    pescado = int(input("Insira a quantidade de peixe pescado"))

    if pescado_total < 150:
        pescado_total = pescado + pescado_total
        if pescado_total >150:
            deitar_fora = pescado_total - 150
            print("Tem de deitar: ", deitar_fora, "toneladas")
            break

    elif pescado_total >= 150:
        pescado_total = pescado + pescado_total

        deitar_fora = pescado_total - 150
        print("Tem de deitar: ",deitar_fora,"toneladas")
        break
