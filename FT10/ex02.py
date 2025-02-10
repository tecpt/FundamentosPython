prov='''o pior cego é aquele
que não quer ver.'''


#Primeira letra da frase em maiúsculas

prov=prov.capitalize()
print(prov)

#Separar as palavras da frase onde ocorre espaço e transformar a frase numa lista
palavras=prov.split(" ")
print(palavras)

#Contar a ocorrência duma palavra numa frase

count=0

for x in palavras:
    if "que" in x:
        count=count+1

print(count)

#Susbstituir uma parte da frase por outra

prov=prov.replace("quer ver", "compra um cão")
print(prov)





