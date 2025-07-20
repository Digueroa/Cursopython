"""
Exercício Python 040: Crie um programa que 
leia duas notas de um aluno e calcule sua média, 
mostrando uma mensagem no final, de acordo com a média atingida:
– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO
"""
nota1=float(input("Digite a primeira Nota?\n"))
nota2=float(input("Digite a seguna Nota?\n"))
media=(nota1 + nota2) / 2
if media < 5 :
    print("Aluno REPROVADO, a sua media foi de {}".format(media))
elif media >= 5 and media < 7:
    print("Aluno em recuperação, sua media foi {}".format(media))
elif media >= 7 :
    print("Aluno APROVADO, a sua media foi de {}, esta de recuperação".format(media))
