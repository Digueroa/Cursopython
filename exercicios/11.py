"""Programa que leia a larguta e altura de uma parede
em metros, calcule a sua área de a quantidade de tinta necessaria para pinta-la
sabendo que cada litro de tinta, pinta uma área de 2m2.
"""
largura=float(input("Digite a largura da parede?\n"))
altura=float(input("Digite a altura da parede?\n"))
area=largura*altura
tinta=area/2
print("A área calculada é {}m² , A quantidade de tinta necessária é de {:.3} Litros".format(area,tinta)) 