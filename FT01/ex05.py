"""Sejam a e b os catetos de um triângulo retângulo, faz um programa que devolva o valor 
da hipotenusa, solicitando os valores dos catetos ao utilizador"""
# Solicitando os valores dos catetos

import math
cateto_a = float(input("Digite o valor do cateto A: "))
cateto_b = float(input("Digite o valor do cateto B: "))
# Calculando a hipotenusa
hipotenusa = math.sqrt(cateto_a ** 2 + cateto_b ** 2) 
# Mostrando o resultado
print("O valor da hipotenusa é: ", hipotenusa)  