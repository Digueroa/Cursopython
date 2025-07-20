""" Desenvolva um programa que lea as duas notas de um aluno
calcule e mostre a sua media"""

nota1=float(input("Digite a Primeira nota\n"))
nota2=float(input("Digite a segunda nota\n"))
soma=nota1+nota2
media=soma/2
print("A media calculada entre as duas notas é {:.1f}".format(media))