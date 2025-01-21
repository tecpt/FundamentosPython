#Verificar se o número é par ou impar
a=int(input("Insira um número:\n->"))
resto=a%2

if resto==0:
    print("O número %f é par" %(a))
else:
    print("O número %f é impar" %(a))