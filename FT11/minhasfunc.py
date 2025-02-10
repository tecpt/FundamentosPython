def triangulo (lado1,lado2,lado3):
    if  lado1==lado2 and lado2==lado3:
        return "Equilátero"
    elif lado1!=lado2 and lado2!=lado3 and lado1!=lado3:
        return "Escaleno"
    else:
        return "Isósceles"
    
def areaeperimetoquadrado(lado):
    area = lado*lado
    perimetro = 4*lado
    return area, perimetro
    

def info_num(*num):
    soma=sum(num)
    total=len(num)
    media=soma/total
    return soma, media, total


def dadoslista(valores):
    soma = sum(valores)
    compr = len(valores)
    media = sum(valores)/len(valores)
    return soma, compr, media


def info_str(palavra="AEc"):
    count_vogais=0
    for x in palavra:
        if x in ["a", "e", "i", "o", "u","A", "E", "I", "O", "U"]:
            count_vogais+=1
    
    return  count_vogais
        
def rep(lista):
    l_rep=[]
    for x in lista:
        if  x not in l_rep:
            l_rep.append(x)
    
    return l_rep



def rep2(lista):
    auxset = set(lista)
    return list(auxset)
        
def mes_v1(num):
    if num==1:
        return "Janeiro"
    if num==2:
        return "Fevereiro"
    if num==3:
        return "Março"
    if num==4:
        return "Abril"
    if num==5:
        return "Maio"
    if num==6:
        return "Junho"
    if num==7:
        return "Julho"
    if num==8:
        return "Agosto"
    if num==9:
        return "Setembro"
    if num==10:
        return "Outubro"
    if num==11:
        return "Novembro"
    if num==12:
        return "Dezembro"
    
def chamar_mes(num):
    match num:
        case "1":
            return "January"
        case "2":
            return "February"
        case "3":
            return "March"
        case "4":
            return "April"
        case "5":
            return "May"
        case "6":
            return "June"
        case "7":
            return "July"
        case "8":
            return "August"
        case "9":
            return "September"
        case "10":
            return "October"
        case "11":
            return "November"
        case "12":
            return "December"
        case _:
            return "Mês Inválido"