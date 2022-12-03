"""
    2) Listar todos os números de 1 a 107 que tenham o digito 7

"""

lista = [x for x in range(1, 108) if str(x).count("7") > 0]

print(lista)


"""
    Obs: 
    1-A questão pede os números que possuem o números 7 com um dos seus algarismo.
    2-A questão fala para avaliar todos os números entre a sêquencia de  1-107, incluindo os terminais
      assim, no metodo range é necessário passar como segundo parâmetro 108, uma vez que o mesmo indica a quantidade e não ultimo elemento da lista
      gerada pelo metodo.
    3-O count é um método de string onde o mesmo busca a presença de uma caracter, que é fornecido pelo parâmetro e retorna a quantidade de vezes que ele esteve presente.
      Portanto, para pode usar esse método é necessário converter o numero em string
    

"""

