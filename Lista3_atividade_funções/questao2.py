"""
2. Escreva uma função onde o usuário pode informar vários dados pessoais (Nome, Sobrenome, CPF e
idade). E imprima somente seu nome e sua idade, caso sejam informados. Se ele não passar nada, não
imprima nada. Entrada: Nome='Júnior', Sobrenome='Limeira', Idade=29, Profissao='Professor'
Saída: Nome: Júnior Idade: 29

"""

def funcao(**kwargs):

    chaves = kwargs.keys()

    if "nome" in chaves and "idade" in chaves:

        print(f"Nome: {kwargs['nome']} Idade: {kwargs['idade']}")


funcao(nome="leandro",sobrenome='Silva',idade=24,profissao='Aluno')

funcao()