"""Faça um algoritmo que leia o ano de nascimento de uma pessoa e o ano atual, depois calcule e 
escreva o número de dias aproximados já vividos por essa pessoa."""

nome=input("Digite seu nome?\n")
anonasc=int(input("Digite o ano de Nascimento?\n"))
anoatual=int(input("Digite o Ano Atual?\n"))
dias=anoatual-anonasc
vividos=dias*365
print("A sua idade é de {}".format(dias))
print("O numero de dias  do(a) {}, e de aproximadamente {}".format(nome,vividos))