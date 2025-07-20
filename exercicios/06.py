""" Crie um algoritmo que leia um numero e mostre
o seu dobro, triplo e raiz quadrada"""

num=int(input("Digite um numero?\n"))
double=num*2
triple=num*3
raiz=num**0.5
print("Analisando o numero {} o seu dobro é {}\ne o seu triplo é {}\ne sua raiz é {:.2f}".format(num,double,triple,raiz))