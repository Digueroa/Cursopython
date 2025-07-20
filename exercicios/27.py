"""
 Faça um programa que leia o nome completo de uma pessoa, 
 mostrando em seguida o primeiro e o último nome separadamente.
"""

nome=str(input("Digite seu nome completo?\n")).strip()
n2=nome.split()
print("O Primeiro nome é {}".format (n2[0]))
print("O Último nome é {}".format (n2[len(n2)-1]))
