"""
Exercício Python 17: Faça um programa que leia 
o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
Calcule e mostre o comprimento da hipotenusa.
"""
from math import hypot
co=float(input("Comprimento do cateto oposto?\n"))
ca=float(input("Comprimento cateto adjacente?\n"))
hi=hypot(co,ca) # hi=(co **2 + ca **2)**(1/2)
print("A hipotenusa vai medir {:.2f}".format(hi))
