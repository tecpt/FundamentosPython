#Alinea a)

Computadores_1={ "Marca":"Asus",
                 "Ecra":"14Pol",
                 "RAM": [4, 8, 12]}

print(Computadores_1["RAM"][1])

#Alinea b)
Computadores_1["Disco"]=["128G", "256G"]
print(Computadores_1)

#Alinea c)
m_ram=int(input("introduza a Capacidade de memoria RAM: "))

#resolução 1
if m_ram in Computadores_1["RAM"]:
    print("existe um computador com essa capacidade")
else:
      print("Não existe um computador com essa capacidade")

#resolução 2
for x in Computadores_1["RAM"]:
    if x==m_ram:
        print("existe um computador com essa capacidade")
        break
else:
    print("Não existe um computador com essa capacidade")


#Alinea d)
Computadores_1["RAM"].append(16)
print(Computadores_1)

#Alinea e)
computadores_2=Computadores_1.copy()

#Alinea f)
computadores_2["Marca"]="Lenovo"
computadores_2["RAM"]=[4,8]
print(computadores_2)


#Alinea g)

computadores_3=Computadores_1.copy()
computadores_3["Marca"]="HP"
computadores_3["Disco"]=["256G"]
print(computadores_3)

#Alinea h)

lista_pc=[Computadores_1, computadores_2, computadores_3]


#Alinea i) - Imprima marca com 128 G de Disco

marcas=""
for x in lista_pc:
    if "128G" in x["Disco"]:
        marcas = marcas + " "+ x["Marca"]
             
print(marcas)      


#Alinea j)

for x in lista_pc:
    if 8 and 12 in x["RAM"]:
        print("Marcas com 8 e 12G de RAM: ", x["Marca"])
