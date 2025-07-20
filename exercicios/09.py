"""Faça um programa que 
leia um numero inteiro qualquer e mostre na tela sua tabuada"""
numero=int(input("Digite um numero?\n"))
#print("{} x {} = {}".format(numero,1,numero*1))
for i in range(1,11):
    resultado=numero*i
    print(f"{numero} x {i}={resultado}")

