'''
Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, 
acrescentando o recurso de mostrar que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes
'''
print('ANALISE DE TRIÂNGULOS')
r1=float(input('Digite o primeiro segmento?\n'))
r2=float(input('Digite o segundo segmento?\n'))
r3=float(input('Digite o terceiro segmento?\n'))
if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print('Os segmentos formam triangulos')
    if r1 == r2 == r3:
        print('EQUILATERO')
    elif r1!=r2!=r3:
        print('ESCALENO')
    else:
        print('ISÓCELES')
