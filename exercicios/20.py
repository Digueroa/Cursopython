"""
Exercício Python 20: O mesmo professor do desafio 19 quer 
sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa 
que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""
from random import shuffle
n1=input("Digite Primeiro nome?\n")
n2=input("Digite segundo nome?\n")
n3=input("Digite o terceiro nome?\n")
n4=input("Digite o quarto nome?\n")
lista=[n1,n2,n3,n4]
shuffle(lista)
print("A ordem sorteada é")
print(lista)