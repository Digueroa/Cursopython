"""
Exercício Python 19: Um professor quer sortear 
um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, 
lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
"""
import random
n1=input("Digite o Primeiro Nome?\n")
n2=input("Digite o segundo nome?\n")
n3=input("Digite o terceiro nome?\n")
n4=input("Digite o quarto nome?\n")
lista=[n1,n2,n3,n4]
escolhida=random.choice(lista)
print("O nome escolhido é {}".format(escolhida))