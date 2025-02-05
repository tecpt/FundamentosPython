#Tomadas de Decisão - 

# if <condicao>: 
#    bloco de instrucoes 1
# else:
#    bloco de instrucoes 2

#Repetição de instruções
# while <condicao>:
#    bloco de instruções
# for <variavel> in <iteravel>:
#    bloco de instruções
#Exemplo de uso de if e else


x = int(input("Introduza um valor:"))
if x > 10:
    print("x é maior que 10")
else:
    print("x é menor ou igual a 10")
    
#Exemplo de uso de while
x = 0
while x < 5:
    print(x)
    x = x + 1 
    
#Exemplo de uso de for
frutas = ['maçã', 'banana', 'laranja']
for fruta in frutas:
    print(fruta)  
    
#Exemplo ciclo for com a função range

aux = range(5) # [0,1,2,3,4]
aux2 =range(1,6) # [1,2,3,4,5]


for x in range(1,21):
    print(x)
 