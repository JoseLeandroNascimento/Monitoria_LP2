"""
9. Crie uma função que recebe um String como parâmetro e verifica se a mesma é composta apenas por
caracteres maiúsculos. A função deve lançar dois tipos de exceções: uma para indicar se existe algum
caractere que não é uma letra e a outra para indicar se algum dos caracteres não é maiúsculo.

"""


# Execeções personalizadas
class NotUpperCaseException (Exception):
    ...

class NotValueAlpha (ValueError):
    ...


# Função que verifica se todos os caracters são maiculos
def isUpperCase(valor: str):

    if not valor.isupper():
        raise NotUpperCaseException(f'{valor} não é maiscula')
    elif not valor.isalpha():
        raise NotValueAlpha(f'{valor} não é composto somente por letras')
    else:

        return True


result = isUpperCase("AAAA1")

print(result)
