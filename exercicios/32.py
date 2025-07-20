"""
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
"""
from datetime import date
ano=int(input("Digite o Ano?\n"))
if ano==0:
    ano=date.today().year
if ano % 100 !=0 and ano % 4 ==0 or ano %400==0:
    print("O ano {} é Bissexto".format(ano))
else:
    print("O ano {} não e Bissexto".format(ano))