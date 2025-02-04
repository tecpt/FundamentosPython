n = input("Introduza um número natural: ")


#Testa se o valor introduzido é um inteiro positivo usando a função isdigit(). Enquanto não for solicita constantemente ao
while not n.isdigit():
    print("O número introduzido é não é válido")
    n = input("Introduza um número natural: ")

n=int(n)


fatorial = 1
for i in range(1,n+1):
    fatorial=fatorial*i

print("fatorial = ", fatorial)