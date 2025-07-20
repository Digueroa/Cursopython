"""
Faça um algoritmo que receba o peso e a altura de uma pessoa
 e informe o valor do seu IMC (Índice de Massa Corporal). Sabe-se que IMC é dado pela 
divisão do peso pela altura ao quadrado.
"""
nome=input("Digite o nome?\n")
peso=float(input("informe o peso?\n"))
altura=float(input("Informe a altura?\n"))
imc=peso/(altura*altura)
print("O IMC do(a) {} é de {:.4}".format(nome,imc))