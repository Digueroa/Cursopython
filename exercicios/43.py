'''
Exercício Python 43: Desenvolva uma lógica 
ue leia o peso e a altura de uma pessoa, 
calcule seu Índice de Massa Corporal (IMC) 
e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida
'''
print('INDICE DE MASSA CORPORAL')
peso=float(input('Digite o seu peso (kg)?\n'))
altura=float(input('Digite a sua altura?\n'))
imc=peso/(altura*altura)
print('O seu IMC é de {:.1f}'.format(imc))
if imc > 18.5 and imc < 25 :
    print('O seu peso está Ideal') 
elif imc > 25 and imc < 30 :
    print('Você está com Sobrepeso')
elif imc > 30 and imc < 40 :
    print('Você esta Obeso')
elif imc > 40 :
    print(' Você esta com Obesidade Mórbida')