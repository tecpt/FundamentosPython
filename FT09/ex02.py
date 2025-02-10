#a.	Cria o dicionário e faz o respetivo print
notas={
"Ana": 10,
"Joaquim": 16,
}

print(notas)

#b.	Acrescenta mais 2 alunos e as respetivas notas
notas.update({"Beatriz": 16.2,"Duarte": 13.5})
print(notas)
#c.	Remove a "ana" da lista
notas.pop("Ana")
print(notas)
#d.	Calcula a média das notas
media=sum(notas.values())/len(notas)
print("A média das notas é: %.2f" %media)

