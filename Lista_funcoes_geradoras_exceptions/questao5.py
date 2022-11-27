
palavras = ['inefevel','grill','faz','batata','ruim','.','A','excecao','é','quando','faz','um','salgado','saboroso']

palavra = []

for x in palavras:

    try:
        palavra.append(x[4])
    except IndexError:
        ...

print(".".join(palavra))