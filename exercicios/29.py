"""
 Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, 
 mostre uma mensagem dizendo que ele foi multado. 
 A multa vai custar R$7,00 por cada Km acima do limite.
"""
velocidade=float(input("Informe a Velocidade?\n"))
limite=80
if velocidade > limite:
   excesso= velocidade - limite
   multa=excesso * 7.00
   print("Você foi Multado!Sua velocidade e {} // O valor da multa é R$ {}".format(velocidade,multa))
print("Velocidade Normal, Siga em Segurança")