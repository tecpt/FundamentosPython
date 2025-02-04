i = 1 #contador
soma = 0 #acumulador

valor = int(input("Enter any positive integer: "))

while i <= valor:
    soma += i
    i += 1
    
print(f'Sum of all numbers till {valor} is ', soma)