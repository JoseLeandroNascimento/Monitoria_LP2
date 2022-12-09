"""
9. Crie uma função anônima que converta uma lista de temperaturas em Celsius para Fahrenheit. Você
deve criar sua função lambda, dentro de uma função map e imprimir as temperaturas com duas casas
decimais. Fahrenheit = 9/5 * Celsius + 32

"""

celsius_to_fahrenheit = lambda list_celsius : list(map(lambda temperatura_celsius: round(9/5 * temperatura_celsius +32,2), list_celsius))

print(celsius_to_fahrenheit([10,0,8,1.23]))

