"""
Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome.
"""

nome=input("Digite o Nome completo?").strip()
print("Analisando seu nome...")
print(nome.upper())
print(nome.lower())
print("Seu nome tem ao todo {} Letras".format(len(nome) - nome.count(" ")))   
#print("Seu primeiro nome tem {} Letras".format(nome.find(" ")))
separa=nome.split()
print("Seu primeiro nome é {} e ele tem {} letras".format(separa[0],len(separa[0])))