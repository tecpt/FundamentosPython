print("""O Índice de Massa Corporal (IMC) é utilizado para medir o peso ideal de uma pessoa.
Escreve um programa que peça o nome, a idade, o peso e a altura do utilizado e que,
de seguida, calcule e mostre o resultado do seu IMC e classifique esse resultado de
acordo com as seguintes condições:
• IMC<17 - Muito abaixo do peso ideal
• 17<=IMC<18,5 - Abaixo do peso
• 18,5<=IMC<25 - Peso normal
• 25<=IMC<30 - Acima do peso
• 30<=IMC<35 - Obesidade I
• 35<=IMC<40 - Obesidade II (severa)
• IMC>=40 - Obesidade III (mórbida)""")


print('Cálculo do IMC')
altura=float(input('Insira sua altura : \n'))
peso=float(input('Insira seu peso : \n'))
imc=peso/(altura*altura)  #poderíamos fazer peso/altura**2
print('Processando seus dados...')
if imc<17:
    print('Muito abaixo do peso.')
elif 17<=imc<18.5:
    print('Abaixo do peso.')
elif 18.5<=imc<25:
    print('Peso normal.')
elif 25<=imc<30:
    print('Acima do peso.')
elif 30<=imc<35:
    print('Obesidade Grau I.')
elif 35<=imc<40:
    print('Obesidade Grau II (severa).')
else:
    print('Obesidade Grau III (mórbida).')
