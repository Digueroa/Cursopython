'''
Exercício Python 45: Crie um programa que faça o 
computador jogar Jokenpô com você.

'''
from random import randint
itens = ('Pedra','Papel','Tesoura')
computador = randint(0 , 2)
print('''SUAS OPÇÕES :
[0] PEDRA
[1] PAPEL
[2] TESOURA ''')
jogador=int(input('QUAL É A SUA JOGADA?\n'))
print('-='*11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*11)