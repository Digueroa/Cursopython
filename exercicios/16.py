"""
Crie um programa que leia um número Real qualquer 
pelo teclado e mostre na tela a sua porção Inteira.
"""
import math
#from math import trunc
num=float(input("Digite um Numero?\n"))
print("O Numero digitado é {} e sua porção inteira é {}".format(num,math.trunc(num))) #(trunc(num))