
datas="12ago2021,02set2020,20jan2022,11out2019,09mar2020,10dez2022"

#alinea a)

l_datas=datas.split(",")
print(l_datas)
#alinea b)

for x in l_datas:
    if "2022" in x:
        print(x)


#alinea c)
dias=[]
for x in l_datas:
    dias.append(int(x[:2]))

dias.sort()
print(dias)






