'''Escreve um programa que receba o nome de um produto e o seu preço, e retorne o preço total considerando os descontos seguintes:

Se o produto for um smartphone, será aplicado um desconto de 10%.
Se o produto for um tablet, será aplicado um desconto de 15%.
Se o produto for um laptop, será aplicado um desconto de 20%.
Para qualquer outro produto, não haverá desconto.

 Utilize a estrutura match...case para determinar o desconto a ser aplicado.
'''
print ("Temos á venda vários produtos:\n")
print ("Smartphones, Tablets, Laptops, Outros")
 
produto = input("Escreva o nome do produto: ").strip().lower()
preco = float(input("Escreva o preço do produto: "))
 
desconto = 0
 
match produto:
    case "smartphone":
        desconto = 0.10
    case "tablet":
        desconto = 0.15
    case "laptop":
        desconto = 0.20
    case _:
        desconto = 0
 
preco_final = preco * (1 - desconto)
print(f"O preço final do {produto} com desconto é: € {preco_final:.2f}")
has context menu