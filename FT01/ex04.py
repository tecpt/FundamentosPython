"""Escreve um programa que calcule o volume de uma esfera. O valor do raio deverá ser 
introduzido pelo utilizador (deverá ser criado o ficheiro ex04.py)."""

import math

raio = float(input("Introduza o raio da esfera: ")) 
volume = (4/3) * math.pi * (raio ** 3)
print("O volume da esfera é: ", round(volume,2) ) # O volume da esfera
