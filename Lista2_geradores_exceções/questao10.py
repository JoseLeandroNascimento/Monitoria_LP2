"""
10. Crie um programa que solicitará uma confirmação: sim ou não, que deverá ser impressa. Considere que
os usuários podem inserir quaisquer valores, você precisa garantir que as diferentes possibilidades sejam
tratadas corretamente. Se uma resposta desconhecida for fornecida, o programa deve gerar uma exceção
personalizada chamada RespostaInvalidaError e forçar que o usuário forneça um valor válido.
"""

class RespostaInvalidaError (Exception):

    ...



while True:

    resposta = input("Confirma?")

    if resposta not in ['sim','não']:

        try:

            raise RespostaInvalidaError(f"Entrada {resposta} não foi reconhecida como comando válido")
        except RespostaInvalidaError as erro:

            print("Entrada invalida")

    else:
        print(resposta)
        break