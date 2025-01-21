print("Insira as medidas dos lados de um triangulo")
a=int(input("lado 1: "))
b=int(input("lado 2: "))
c=int(input("lado 3: "))

if a==c and c==b:
    print("o triangulo é equilátero")
elif a!=c and a!=b and b!=c:
    print("o trianguloo é escaleno")
else:
    print("o triangulo é isósceles")