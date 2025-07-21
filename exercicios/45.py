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
if computador == 0: #Computador jogou PEDRA
    if jogador ==0:
        print('Empate')
    elif jogador ==1:
        print('Jogador Vence')
    elif jogador ==2:
        print('Computador Vence')
    else:
        print('JOGADA INVÁLIDA')

    
elif computador == 1:# Computador Jogou PAPEL
     if jogador == 0:
         print('Computador Vence')
     elif jogador ==1:
         print('Emapte')
     elif jogador ==2:
         print('Jogador Vence')
     else:
         print('JOGADA INVÁLIDA')

elif computador == 2: #Computador Jogou TESOURA
    if jogador == 0:
        print('Jogador Vence')
    elif jogador ==1:
        print('Computador Vence')
    elif jogador ==2:
        print('Empate')
    else:
         print('JOGADA INVÁLIDA') 
         