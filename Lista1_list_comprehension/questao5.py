

"""

5) Obtenha apenas os números de uma frase


"""

# SOLUÇÂO 1

frase = "O rato roeu 1 roupa do rei de Roma e foi condenado a 100 anos de prisão"

lista_numero = [token for token in frase.split() if token.isdecimal()]

print(lista_numero)

"""
    O metodo split retorna todas palavra em um array. Isso é necessário, pois,
    O for iria obter uma letra por vez, sendo assim o número 100 não seria reconhecido como um número unico,
    mas com os números 1,0,0, para evitar isso, obter as palavras de frase e depois analizar se a mesma é um numero

"""

# SOLUÇÂO 2

frase = "O rato roeu 1 roupa do rei de Roma e foi condenado a 100anos de prisão"

lista_numero = [token for token in frase if token.isdecimal()]

print(lista_numero)

"""
    Caso o contexto número não import essa solução seria a mais correta, afinal de contas um número 
    poderia fazer parte de uma palavra. Já que no exeplo da frase acima a expressão "100anos" não seria consiredada pela solução 1
"""