"""
Crie um programa que leia um número inteiro 
e mostre na tela se ele é PAR ou ÍMPAR.
"""
numero=int(input("Digite um numero?\n"))
if numero % 2 == 0:     # resultado = numero % 2
    print("Numero Par")  #if resultado ==0
else: 
    print("IMPAR")