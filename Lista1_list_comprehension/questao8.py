"""
8) Use dicionário para contar a quantidade de caracteres de cada palavra de uma frase

"""

frase = "O rato roeu 1 roupa do rei de Roma e foi condenado a 100 anos de prisão"

lista = [{"palavra":palavra,"quantidade_letra":len(palavra)} for palavra in frase.split()]

print(lista)

"""
    Dicionario é um tipo dado que armazena dados indexado por uma chave, sendo assim para acessar
    Os seus valores tem que saber chave correndo a valor desejado
"""