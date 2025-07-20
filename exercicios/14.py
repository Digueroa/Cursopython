"""
Escreva um programa que converta uma temperatura digitando em graus 
Celsius e converta para graus Fahrenheit.

"""
temp=float(input("Digite o valor da Temperatura em graus Celsius\n"))
far=((temp*9)/5)+32
print(" A temperadura de {} graus Celsius ,corrensponde a {} fahrenheit".format(temp,far))