
idades=[25, 15, 19, 22, 37, 78, 46, 2, 67]
#a.	Indique quantas pessoas são menores de idade
count=0
for x in idades:
    if x<18:
        count=count+1

print("O numero de pessoas menores de idades é:", count)

#c.	Ordene a lista por ordem decrescente
idades.sort(reverse=True)
print(idades)

#d.	Pede ao utilizador uma idade e verifica se essa idade está na lista. 
#- Se estiver faz print("A idade está na lista")
#- Caso contrário faz o print("não existe ninguém com essa idade na lista")

a=int(input("Introduza a idade a pesquisar: "))
if a in idades:
    print("A idade ", a, "está na lista.")
else:
    print("A idade ", a, "não está na lista.")


