

"""
9) Dada uma lista com os nomes de 5 pessoas, liste um conjunto de tuplas de todas as
combinações com 2 pessoas diferentes

"""

nomes = ['Leandro','Laires','Bruna',"Lucas", "Felipe"]

lista_combinacoes = [(nome1,nome2) for nome1 in nomes for nome2 in nomes if nome1!=nome2]


print(lista_combinacoes)

"""
    Lista comprehension aceita for encadeados, como se fosse assim:

    lista_combinacoes = []

    for nome1 in nomes:

        for nome2 in nomes:

            if nome1 != nome2

                lista_combinacoes.append((nome1,nome2))

"""

