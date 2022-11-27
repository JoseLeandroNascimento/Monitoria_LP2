
import random


def sorteadorMegaSena(quantidade):

    numeros_sorteados = []

    cont = 0
    while cont <= quantidade:

        numero = random.randint(1,60)

        if numero is not numeros_sorteados:

            cont+=1
            numeros_sorteados.append(numero)

            yield numero


for x in sorteadorMegaSena(6):

    print(x)

