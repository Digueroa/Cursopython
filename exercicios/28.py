"""
Exercício Python 28: Escreva um programa que faça o 
computador “pensar” em um número inteiro entre 0 e 5 
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
 O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""
import random
from time import sleep
nupc=random.randint(0,5)
print("-=-"*20)
print("Vou Sortear um numero de 0 à 5 tente adivinhar...")
print("-=-"*20)
nu=int(input("Pense me um Numero?\n"))
print(" PROCESSANDO...")
sleep(3)
if nu==nupc:
    print("Acertou")
else:
    print("Errou")
print("O Numero digitado foi {},e o sorteado foi {}".format(nu,nupc))