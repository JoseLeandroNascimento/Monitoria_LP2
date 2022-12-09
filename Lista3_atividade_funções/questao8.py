"""
8. Utilize a função map para imprimir o tamanho e a quantidade de vogais de cada palavra de uma frase.
"""
from functools import reduce
VOGAIS = ['a','e','i','o','u']

FRASE = "O rato roeu a roupa do rei de Roma"


saida = list(map(lambda palavra: f"Palavra: {palavra} - tamanho: {len(palavra)} - N vogais {reduce(lambda quantidade,letra: quantidade + palavra.lower().count(letra) ,VOGAIS,0)}",FRASE.split()))

print(*saida,sep="\n")