
from functools import reduce

# Solução 1

def somatorio1(lista = []):

    # Navega entre a lista de tuplas
    # Onde cada item é uma tupla de números
    for item in lista:

        # Utilizando a função reduce para percorrer a tupla e somar seus elementos
        total = reduce(lambda x,y: x +y, item, 0)        
        
        yield total



resultado = somatorio1([(1,2,3),(5,7),(99,15,-5)])

print(*list(resultado),sep=" ")

# ######################################################################

# Solução 2
def somatorio2(lista = []):

    # Navega entre a lista de tuplas
    # Onde cada item é uma tupla de números
    for itemTupla in lista:

        total = 0

        # Soma todos os elementos da tupla
        for item in itemTupla:

            total += item

        yield total

resultado = somatorio2([(1,2,3),(5,7),(99,15,-5)])

# Imprime o resultado
print(*list(resultado),sep=" ")


# ######################################################################
