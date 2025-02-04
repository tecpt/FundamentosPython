#Utilizando estruturas de repetição escreva um programa que mostre os
#resultados da tabuada de multiplicação dos números entre 1 e 10, como segue.

for valor in range(1,11):
    for numero in range(1,11):
        print('%d X %d = %d'%(valor,numero,valor*numero))
    print("------------------------")