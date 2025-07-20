"""Escreva um programa que leia um valor em metros e o exiba convertido
em centimetros e milimetros"""
metros=float(input("Digite o valor em metros desejado?\n"))
cent=metros*100
mili=metros*1000
print("O valor analisado  {} em metro, corresponde a {:.0f} Centimetros e a {:.0f} Milimetros".format(metros,cent,mili))