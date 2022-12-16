
"""
2. Dada uma lista de tuplas que contém nome, departamento, idade, salário dos funcionários de uma
empresa, por exemplo: [('Chaves', 'TI', 23, 2900), ('kiko', 'RH', 45, 3376), ('Madruga', 'EAD', 19, 1550),
('Nhonho', 'EAD', 31, 3300), ('chiquinha', 'RH', 15, 732), ('Florinda', 'TI', 55, 4500), ('Girafales', 'RH', 49,
2000)].
Liste os funcionários em ordem crescente pelo departamento e depois em ordem decrescente de salário.
Escreva uma função para aumentar os salários dos funcionários em 13% do valor atual.
Crie uma função para imprimir o total de funcionários e da folha de pagamento da empresa.

"""
from functools import reduce

def promocao(lista):
    
    return [(item[0],item[1],item[2],round(item[3]*1.13,2)) for item in lista]

def infoEmpresa(dataList):

    totalFuncionario = len(dataList)
    totalFolhaPagamento = reduce(lambda x,y:x+y[3],dataList,0.0)

    print(f"Total de funcionarios: {totalFuncionario} - Folha de pagamento total: {totalFolhaPagamento}")


lista = [('Chaves', 'TI', 23, 2900), ('kiko', 'RH', 45, 3376), ('Madruga', 'EAD', 19, 1550),
('Nhonho', 'EAD', 31, 3300), ('chiquinha', 'RH', 15, 732), ('Florinda', 'TI', 55, 4500), ('Girafales', 'RH', 49,
2000)]

# Listando funcionario em crescente pelo departamento
print("Nome","Departamento","Idade","salario",sep="  ")
print(*lista,sep='\n')

lista.sort(key=lambda item: item[1])
print()
print("Ordem de Departamento:")
print(*lista,sep='\n')

# Ordenar em ordem decrescente de salário


lista.sort(key=lambda item:item[3],reverse=True)
print()
print("Ordem de salario:")
print(*lista,sep='\n')

# Aplicando promoção


lista = promocao(lista)

print()
print("Aumento de salario:")
print(*lista,sep='\n')

print()
infoEmpresa(lista)