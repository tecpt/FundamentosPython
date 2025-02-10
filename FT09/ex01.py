
menu={
        "entremeada": 7,
        "Sardinha": 6,
        "Filetes": 5.5,
        "Prego": 7,
        "Hamburguer": 5.5
}


#a.	Faz o print do preço do "prego"
print("O preço do prego é: ", menu.get("Prego"))
#b.	Faz o print de todas as chaves do dicionário
print(menu.keys())

for key in menu.keys():
        print(key)

#c.	Acrescenta na lista "omolete" com um preço de 5
menu.update({"omolete": 5})
print(menu)

#d.	Faz o print todo o dicionário para visualizar as alterações
print(menu)


#EXTRA.	Muda o preço do "prego" para 10

menu.update({"Prego":10})
print(menu)




