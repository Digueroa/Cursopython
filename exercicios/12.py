"""Faça um algoritmo que leia o preço de um produto e mostre 
seu novo preço,com 5% de desconto"""

produto=float(input("Digite o valor do Produto?\nR$"))
preco=produto*5/100   #preco=produto- (produto*5/100)
desconto=produto-preco
print("O Valor do Produto com Desconto é R${:.5}".format(desconto))
print("O valor do desconto é R${:.2}".format(preco))