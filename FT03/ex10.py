operacao=input('Escolha a operação: (+,-,*,/)')
   
num1=float(input('Número 1: '))
num2=float(input('Número 2: '))

if operacao=='+':
    soma = num1+num2
    print("%s+%s=%s"%(num1,num2,soma))
elif operacao=='-':
    subtracao = num1-num2
    print("%s-%s=%s"%(num1,num2,subtracao))
elif operacao=='*':
    multiplicacao = num1*num2
    print("%s*%s=%s"%(num1,num2,multiplicacao))
else:
    if num2==0:
        print('O denominador precisa ser diferente de zero.')
    else:
        divisao = num1/num2
        print("%s/%s=%s"%(num1,num2,divisao))
        

