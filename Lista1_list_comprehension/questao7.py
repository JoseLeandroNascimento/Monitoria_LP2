import random

"""
7) Retorne uma lista de tuplas onde o primeiro valor é um inteiro de 1 até 100 e o
segundo valor é um número aleatório entre 0 e 100 quando o primeiro é ímpar, caso
contrário será a string "par"
"""

lista = [(numero, random.randint(0,100) if numero%2!=0 else 'par') for numero in range(1,101)]

print(lista)

"""
    Explicando o funcionamento da expressão "random.randint(0,100) if numero%2!=0 else 'par'"
    
    valo1 if expressao_logica else valor2

    Caso a expressao_logica seja verdadeira o valor 1 é retornado, caso seja falsa o valor2 é retornado
"""