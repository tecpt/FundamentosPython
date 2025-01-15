a =int( input("Introduza um número\n->"))
b = int(input("Introduza outro número\n->"))
soma= a+b

print("o resultado de somar",a, " com", b, "é", soma)

print(f"o resultado de somar {a} com {b} é {soma}") # mais eficiente

print("o resultado de somar {} com {} é {}".format(a,b,soma))

print("o resultado de somar %d com %d é %d"%(a,b,soma))  #%d inteiro %f float %s string

