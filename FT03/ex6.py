numero1=float(input('Número 1: '))
numero2=float(input('Número 2: '))
numero3=float(input('Número 3: '))



if (numero1>numero2) and (numero1>numero3):
    print("Maior número:",numero1)
elif (numero2>numero1) and (numero2>numero3):
    print("Maior número:",numero2)
elif (numero2==numero1) and (numero2==numero3):
       print("Os números são iguais")
else:
    print("Maior número:",numero3)
