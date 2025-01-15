""" Escreve  um  programa  que  solicite  a  temperatura  em  Fahrenheit  (F),  ao  utilizador,  e  a 
converta para grau Celsius (C), devolvendo o resultado da conversão. 
 
Use a fórmula: C = 5 * ((F-32) / 9)"""


f=float(input('Temperatura em Fahrenheit: \n'))
c=5*((f-32)/9)
print("%f F equivale a %f Cº ."%(f,c))      