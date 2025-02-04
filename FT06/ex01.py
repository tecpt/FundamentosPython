
cores=["amarelo", "azul", "branco", "preto", "verde"]

#a.	Faz o print de toda a lista
print(cores)

#imprimir elemento a elemento
for cor in cores:
    print(cor)
    
#b.	Faz o print da posição 2 da lista
print(cores[2])

#c.	Altera a posição 0 da lista para "vermelho"
cores[0]="vermelho"

#d.	Faz o print de toda a lista
print(cores)

#e.	Acrescenta no final da lista a cor "amarelo"
cores.append("amarelo")

#f.	Faz o print de toda a lista
print(cores)

#g.	Acrescenta na posição 2 a cor "roxo"
cores.insert(2, "roxo")

#h.	Faz o print de toda a lista
print(cores)


#i.	Apaga o último elemento da lista
cores.pop()
#j.	Faz o print de toda a lista
print(cores)
#k.	Faz o print do tamanho da lista (len)
print(len(cores))