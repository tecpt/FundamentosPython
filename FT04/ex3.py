
'''Fazer um programa para ler quatro números inteiros e positivos, calcular e devolver  a  sua 
média. - usando o ciclo while'''

x =0
soma = 0
while x < 4:
    num = int(input("Digite um número: "))
    soma += num
    x += 1

media = soma / 4
print(media)

'''Fazer um programa para ler quatro números inteiros e positivos, calcular e devolver  a  sua 
média usando o ciclo for'''

soma2=0
for x in range(5):
    num = int(input("Digite um número: "))
    soma2 += num # soma2 = soma2 + num
    
media2 = soma2 / 4
print(media2)
    