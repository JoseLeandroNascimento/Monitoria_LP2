"""
6. Usando uma função anonima receba dois argumentos iteráveis e retorne a potência de cada elemento do
primeiro argumento elevado ao elemento correspondente no segundo argumento.

"""

funcao_anonima = lambda iter1,iter2: list(map(lambda item1,item2: item1**item2,iter1,iter2))

print(funcao_anonima([1,2,3,4],[2,2,2,2]))