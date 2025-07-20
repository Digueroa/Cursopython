'''
Exercício Python 44: Elabore um programa que calcule o 
valor a ser pago por um produto, considerando
 o seu preço normal e condição de pagamento:

 – à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal 

– 3x ou mais no cartão: 20% de juros
'''
print('WELCOME TO THE HALL OF DISCOUNT')
valor=float(input('Digite o valor a Pagar R$?\n'))
print('''FORMAS DE PAGAMENTO
[1] á vista dinheiro/cheque
[2] á vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opcao =int(input('Qual é a opção?\n'))
if opcao == 1:
    total= valor - (valor * 10 / 100)
elif opcao == 2:
    total = valor - (valor * 5 / 100)
elif opcao == 3:
    total=valor
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opcao == 4:
    total = valor + (valor * 20 / 100)
    totalparc=int(input('Quantas parcelas?\n'))
    parcela =total / totalparc
    print('Sua compra será parcelada {} de R$ {:.2f}'.format(totalparc,parcela))

print('Sua compra de R${:.2f} vai custa R${:.2f} no final'.format(valor,total))



