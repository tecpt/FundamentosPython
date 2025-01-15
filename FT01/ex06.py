"""Faz  um  programa  que  receba  três  parâmetros  inteiros  (horas,  minutos  e  segundos)  e 
converta  o  resultado  para  segundos,  devolvendo  o  output  para  o  ecrã sem urilizar a funções"""

   
horas = int(input("Insira o número de horas: "))
minutos = int(input("Insira o número de minutos: "))
segundos = int(input("Insira o número de segundos: "))

total_segundos = (horas * 3600) + (minutos * 60) +segundos

print(f"O total de segundos é {total_segundos}")




