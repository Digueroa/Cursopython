"""
Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, 
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se 
é a hora exata de se alistar ou se já passou do tempo do alistamento.
 Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

"""
from datetime import date
atual=date.today().year
nasc=int(input("Digite o Ano de nascimento?\n"))
sexo=str(input("Digite o Sexo? ( M para masculino, F para feminino)")).strip().upper()
idade=atual-nasc
print("Quem nasceu em {} tem {} anos em {}.".format(nasc,idade,atual))

if idade == 18 and sexo == "M" :
    print("Você tem que se alistar IMEDIATAMENTE")
elif sexo == "F":
    print("Alistamento não obrigatorio para Mulheres")
elif idade < 18 and sexo == "M" :
    saldo=18-idade
    print("Ainda nao tem 18 anos. Ainda faltam {} anos".format(saldo))
    ano=atual+saldo
    print("Seu alistamento será em {}".format(ano))
elif idade > 18 and sexo == "M":
    saldo=idade-18
    print("Voce ja deveria ter alistado há {} Anos".format(saldo))
    ano=atual-saldo
    print("Seu alistamento foi em {}".format(ano))




