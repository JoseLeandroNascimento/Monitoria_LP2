"""
4) Crie uma lista de todas as consoantes de uma frase

"""
VOGAIS = ('a','e','i','o','u')

frase = "O rato roeu a roupa do rei de Roma"

lista_consoantes = [letra for letra in frase if letra.isalpha() and  letra.lower() not in VOGAIS]

print(lista_consoantes)

"""
    Explicação:

    1- letra.isalpha(): verifica se um caracter é uma letra, assim ignora caracteres númericos e outros como espaço e $, por exemplo.
    2- letra.lower() not in VOGAIS: Essa expressão atraves dos operadores not in retorna true se o elemento da esquerda não estiver contido no interavel da direita
    3- letra.isalpha() and  letra.lower() not in VOGAIS: Essa duas condições são necessária para obter e encapsular as consoante de uma frase em uma lista

    Obs:

    A estratégia de listar somente as vogais evitar de ter que listar todas as consoantes, o que seria mais demorado,
    Como nós temos apenas as categoria de vogais e consoante, se uma letra não for de um tipo será de outro
"""