
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
