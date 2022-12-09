"""
7. Usando uma função anonima que receba dois argumentos iteráveis e a função filter(), encontre os
valores que são comuns nos dois argumentos.

"""

intercept = lambda iter1,iter2: list(filter(lambda item: item in iter2,iter1))

print(intercept([1,21,13,4],[2,3]))