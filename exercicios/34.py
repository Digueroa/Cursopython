"""
 Escreva um programa que pergunte o salário 
 de um funcionário e calcule o valor do seu aumento. 
 Para salários superiores a R$1250,00, calcule um aumento de 10%. 
 Para os inferiores ou iguais, o aumento é de 15%.
"""
salario=float(input("Digite o Valor do Salario?\n"))
if salario > 1250 :
    calculo=salario * 0.1
    aumento=calculo + salario  # aumento=salario + (salario * 10 / 100)
if salario <= 1250 :
    calculo=salario * 0.15
    aumento=calculo + salario  # aumento=salario + (salario * 15 / 100)
print("O seu sálario e R${} o aumento vai ser de R${} ".format(salario,aumento))