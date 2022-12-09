"""
1. Escreva duas funções que aceitem qualquer quantidade de números reais e retorne a multiplicação desses
números (Uma função usando o laço for e outra usando reduce).

"""

from functools import reduce

def funcao1(*args):

    total = 1

    for valor in args:

        total*=valor

    return total


def funcao2(*args):

    return reduce(lambda x,y: x*y,args)



print(funcao1(1,2,3,4))
print(funcao2(1,2,3,4))