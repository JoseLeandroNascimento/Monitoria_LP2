"""
10. Utilize a função reduce para imprimir a concatenação das palavras de uma lista, com um espaço em
branco entre as palavras.

"""

from functools import reduce

nomes = ['Leandro','Laires','Maria',"João"]

result = reduce(lambda concatenacao,palavra: f"{concatenacao} {palavra}",nomes)

print(result)

