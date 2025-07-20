"""Programa que leia quanto dinheiro uma pessoa tem na carteira
e mostre quantos dolares ela pode comprar , considere USS1,00 = R#3,27"""

carteira=float(input("Digite o valor da carteira? R$\n"))
dolar=carteira/3.27
real=carteira*3.27
print("Analisando o valor da carteira R${}, voce podera comprar U$${:.4} dolares".format(carteira,dolar))
print("Analisando o valor da cartiera U$${}, voce podera compra R${:.4} reais".format(carteira,real))