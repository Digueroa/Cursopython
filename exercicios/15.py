"""
Escreva um programa que pergunte a quantidade de Km percorridos 
por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, 
sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
"""
km=float(input("Informe a quantidade de KM percorridos?\n"))
dias=int(input("Informe a quantidade de dias alugado?\n"))
valorkm=km*0.15   #total=(dias*60)+(km*0.15)
valordias=dias*60
total=valorkm+valordias
print("O valor a ser pago por KM é R${} e pelos dias locado R${}".format(valorkm,valordias))
print("O valor total a ser Pago é {}".format(total))
