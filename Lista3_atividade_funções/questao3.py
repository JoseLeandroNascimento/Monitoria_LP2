"""
3. Desenvolva uma função que aceite qualquer e tipo número de argumentos posicionais (*args) e palavras-
chave com valores (**kwargs) e que imprima os argumentos posicionais na ordem inversa de entrada e as
palavras-chave com seus valores em ordem alfabética.

"""

def funcao(*args, **kwargs):

    print(args[::-1])

    ordenAlpha = { chave:valor for chave,valor in sorted(kwargs.items(),key=lambda item: item[1])}

    print(ordenAlpha)


funcao(1,2,3,4,5,arg1="d",arg2='sd',arg3='ja')

"""
Obs:

- kwargs.items(): retorna uma lista de tupla com dois valores, onde o primeiro é a chave e o segundo o valor do dicionário

- sorted: essa função é responsável por ordenar os valores da tupla em ordem crescente, porém para informa isso temos que passa uma função 
  lambda como parâmentro para key, que por sua vez entende que é para ordenar o dicionario com base no valor e, não na chave como de padrão.
  Isso é feito pela expressão "lambda item: item[1]", na qual o item[1] informa explicitamente a posição de cada item da tista de tuplas,
  sendo a posição 1 onde se encontra o valor do dicionario. Por fim um novo dicionario é criado, ordenado por ordem alfabetica





"""