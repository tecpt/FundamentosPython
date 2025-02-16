def lista(valores):
    soma= sum(valores)
    nelem= len(valores)
    med= soma/nelem
    return (soma, nelem, med)
serie=[]
serie.append(float(input("Introduzo o 1º elemento sa serie de números: ")))
i = 2
while i >0:
    inp = input("Introduzo o %iº elemento sa serie de números: " %i)
    if inp == "": break
    i +=1
    serie.append(float(inp))
    
res = lista(serie)
print("Soma: ", res[0])
print("Número de elementos: ", res[1])
print("Média: ", res[2])