"""
6) Encontre todas as palavras em uma frase com mais de 5 letras

"""

frase = "O rato roeu 1 roupa do rei de Roma e foi condenado a 100 anos de prisão"

lista = [x for x in frase.split() if len(x)>5]

print(lista)

"""
    Função len retiorna a quantidade de elemento de uma string, para isso dá certo é necessário pegar cada palavra da frase
    para isso usa-se o método split
"""
