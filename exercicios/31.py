"""
Desenvolva um programa que pergunte a distância de uma viagem em Km.
 Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de 
 até 200Km e R$0,45 parta viagens mais longas.
"""
km=float(input("Digite a distancia da sua viagem?\n"))
if km <= 200:
    preco=km*0.50
else:
    preco=km*0.45
print("O valor da viagem é de R${:.2f} reais".format(preco))
