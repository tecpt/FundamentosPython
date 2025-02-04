from statistics import mean


notas=[11.2, 15, 8.7, 17.2, 7.9 ]

notas.append(10.9)

print(f"A lista inclui os seguintes elementos{notas}")
print(f"O número de elementos na lista é é {len(notas)}")
print(f"A nota mínima é {min(notas)}")
print(f"A média das notas é {mean(notas)}")