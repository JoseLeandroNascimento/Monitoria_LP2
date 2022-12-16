"""

1. Escreva uma função que receba 4 valores inteiros (i, j, k, n) como entrada e forneça uma lista de tuplas
com todas as combinações uma lista de todas as coordenadas possíveis dadas por (i, j, k) em um plano 3D
onde a soma de i+j+k não é igual a n. Use list comprehension para resolver a questão.
Entrada: 1, 1, 2, 3
Saída: [(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 2)]

"""

def funcao(i,j,k,n):

    coordenadas = [(x,y,z) for x in range(i+1) for y in range(j+1) for z in range(k+1) if x + y + z != n]

    return coordenadas

print(funcao(1,1,2,3))