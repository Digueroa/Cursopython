"""
Exercício Python 25: Crie um programa que leia 
o nome de uma pessoa e diga se ela tem “SILVA” no nome.
"""
nome=str(input("Digite seu Nome?")).strip()
if "silva" in nome.lower():
    print("Você e um Silva")
else:
    print("Você nao e um Silva")


