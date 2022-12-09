"""

4. Faça um programa que solicite seis números do usuário e exiba apenas os números maiores do que 6.
Utilize a função filter para fazer isso.

"""

lista_numero = []

for x in range(6):

    lista_numero.append(int(input(f"Número {x+1}: ")))


lista_resposta = list(filter(lambda item: item > 6,lista_numero))

print(lista_resposta)


