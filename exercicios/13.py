"""Um algoritmo que leia o salario de um funcionario e mostre
seu novo salario, com 15% de aumento"""
funcionario=input("Digite o nome do funcionário?\n")
salario=float(input("Digite o Salario?\nR$"))
nvasalario=salario+(salario*15/100)
print("O salario do funcionario {} era de {} , com o aumento de 15% é R${:.2f}".format(funcionario,salario,nvasalario))