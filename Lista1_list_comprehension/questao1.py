
"""
 1) Listar os números de 1 a 10*7 que são divisíveis por 7

 A questão pede que seja gerado uma lista com elementos que são divisiveis por 7
 OBS:
    Um número só é divisivel por outro número quando o resto da sua divisão é 0
    ex: 10 dividido por 7 é 1 e seu resto é 3.
    no puthon para saber o resto de uma divisão tempos o operador "%"


"""


lista = [x for x in range(1, 10**7) if x % 7 == 0]


"""
    passo a passo da execução da expressão acima:

    passo 1: 

        O metodo range retorna um interavel com as configurações passadas em seu parâmetros,
        o primeiro parametro indica qual o primeira elemento, o segundo parâmetro indica a 
        quantidade de elementos que serão gerados o terceiro parâmetro indica o salto que é dado
        de um elemento para outro, caso seja passado somente um parâmetro para o metodo range
        os valores do primeiro elemento será 0 e o salto será 1

    passo 2:

        O for percorre cada elemento do interavel

    passo 3: 

        Cada elemento do interável passa pela expressão logica, caso a mesma seja atendida o mesmo
        passa para o passo 4 

    passo 4:

        cada elemento é adicionado na lista

    passo 5:

        pula para o passo 2. Assim faz até que o interavel seja consumido por completo
"""

