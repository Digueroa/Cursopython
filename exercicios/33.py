"""
Faça um programa que leia três números 
e mostre qual é o maior e qual é o menor.
"""
n1=int(input("Digite o primeiro Numero?\n"))
n2=int(input("Digite o segundo Numero?\n"))
n3=int(input("Digite o segundo Numero?\n"))
#verificando o menor
if n1<n2 and n1 <n3:
    menor=n1
if n2<n3 and n2 <n1:
    menor=n2
if n3<n1 and n3<n2:
    menor=n3
#verificando o maior
if n1>n2 and n1>n3:
    maior=n1
if n2>n3 and n2 >n1:
    maior=n2
if n3>n1 and n3>n2:
    maior=n3
    
print("O Numero menor é {}".format(menor))
print("O Numero maior é {}".format(maior))