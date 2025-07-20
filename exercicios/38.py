"""
Exercício Python 038: Escreva um programa que leia dois 
números inteiros e compare-os. mostrando na tela uma mensagem:
– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais

"""
num1=int(input("Digite o Primeiro numero:\n"))
num2=int(input("Digite o Segundo Numero:\n"))
if num1 > num2:
    print("O Primeiro Valor e maior")
elif num2 > num1:
    print("O Segundo valor e maior")
else:
    print("Numeros Iguais")