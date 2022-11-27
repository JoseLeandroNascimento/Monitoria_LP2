
import random


def sorteadorMegaSena(quantidade):

    # Quarda referência dos número já sorteados
    # Evitando que o mesmo seja sorteado novamente
    numeros_sorteados = []

    # Conta a quantidade de números sorteados
    cont = 0

    while cont <= quantidade:

        # Gera um número aletóario entre 1 - 60
        numero = random.randint(1,60)

        # Verifica se o número gerado já foi sorteado
        if numero is not numeros_sorteados:

            # Caso o número seja valido, é contado um número gerado
            # e o mesmo é adicionado na lista do números sorteados
            cont+=1
            numeros_sorteados.append(numero)
            
            # Retorna o valor gerado
            yield numero


for x in sorteadorMegaSena(6):

    print(x)

