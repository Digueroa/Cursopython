"""
Exercício Python 041: A Confederação Nacional de Natação 
precisa de um programa que leia o ano de nascimento 
de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER
"""
from datetime import date
atual=date.today().year
print("BEM VINDO CONFEDERAÇAO NACIONAL DE NATAÇÃO!!!")
ano=int(input("Digite o Ano de Nascimento?\n"))
idade=atual-ano
print("O Alteta tem {}".format(idade))
if idade >=1 and idade <=9 :
    print("CATEGORIA MIRIM")
elif idade >=10 and idade <= 14 :
    print("CATEGORIA INFANTIL")
elif idade >=15 and idade <=19 :
    print("CATEGORIA JUNIOR")
elif idade >=20 and idade <=25 :
    print("CATEGORIA SENIOR")
elif idade > 25 :
    print("CATEGORIA MASTER")