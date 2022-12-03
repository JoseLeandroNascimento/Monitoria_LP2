"""
10) Dado um dicionário qualquer, obtenha outro dicionário onde as chaves serão os
valores e vice-versa.

"""

dados_pessoais = {"nome":"Leandro","idade":24,"sexo":"masculino"}

pessoais_dados = { dados_pessoais[chave]:chave for chave in dados_pessoais}

print(dados_pessoais)
print(pessoais_dados)

"""
    pessoais_dados = {}

    for chave in dados_pessoais:

        # quando uma chave inexistente é fornecida ao inserir um novo elemento para um dicionário ela é criada
        
        pessoais_dados[chave] = chave
"""