"""Faz  um  programa  que  receba  a  distância  em  km  e  a  quantidade  em  litros  de 
combustível consumido por um carro num percurso. Calcula o consumo km/l e escreve 
uma  mensagem  de  acordo  com  o  resultado  obtido. """

# Recebe a distância em km e a quantidade em litros de combustível consumido por
# um carro num percurso
distancia = float(input("Digite a distância em km: "))
litros = float(input("Digite a quantidade em litros de combustível consumido: "))

# Calcula o consumo km/l
consumo = distancia / litros

print(f"O número de kms percorrido por litro de combustível é {consumo}")




