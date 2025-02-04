
nums=[10, 2.5, 7, 11, 7.9, "Python", True,6, 5.8 , "Listas"]


#Alinea a)
c_int=0
c_float=0
c_str=0
c_bool=0
for x in nums:
    if type(x)==int:
        c_int=c_int+1
        continue
    if type(x)==float:
        c_float=c_float+1
        continue
    if type(x)==str:
        c_str=c_str+1
        continue
    if type(x)==bool:
        c_bool=c_bool+1

print("quantidade de inteiros na lista= ", c_int)
print("quantidade de floats na lista= ", c_float)
print("quantidade de Strings na lista= ", c_str)
print("quantidade de Booleanos na lista= ", c_bool)

#Alinea b)
soma=0
count=0
for x in nums:
    if type(x)==int:
        soma = soma +x
        count=count+1

media=soma/count
print("A media dos valores inteiros é: ", media)

#Alinea c)
nova_lista=[]
for x in nums:
    if type(x)==int:
        nova_lista.append(x)


print(nova_lista)



