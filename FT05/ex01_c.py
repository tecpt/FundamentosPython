'''Escreva um programa que gere 100 números reais aleatórios entre 0 e 1 e
armazene
os numa lista . No final o programa deverá mostrar as seguintes
informações:
i. Maior número;
ii. Menor número;
iii. Soma de todos os números gerados;
iv. Média e desvio padrão.'''

from random import random
from statistics import mean, stdev

lista = []
for num in range(1,101):
    lista.append(random())

print(lista)
print("...................")
print('O Máximo é:', max(lista))
print('O Mínimo é:', min(lista))
print('A Soma Total é:', sum(lista))

print('A Média Total é:', sum(lista)/len(lista))

print('A Média Total é:', mean(lista))
print('O desvio de padrão é:', stdev(lista))
print("...................")