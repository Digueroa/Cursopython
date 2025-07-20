"""
Escreva um programa para aprovar o empréstimo bancário 
para a compra de uma casa. Pergunte o valor da casa, 
o salário do comprador e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário ou 
então o empréstimo será negado.
"""
print("-="*30)
valorcasa=float(input("Qual o valor da casa?R$\n"))
salario=float(input("Digite seu salario?R$\n"))
anos=int(input("Digite em quantos anos deseja pagar?\n"))
print("-="*30)
mensalidade=valorcasa / (anos * 12)
minimo=salario * 30 / 100
print("Parapagar um casa de R$ {:.2f} em {} anos a mensalidade sera de R${:.2f}".format(valorcasa,anos,mensalidade))
if mensalidade <=minimo:
    print("Emprestimo pode ser CONCEDITO!")
else:
    print("Emprestimo NEGADO!")

