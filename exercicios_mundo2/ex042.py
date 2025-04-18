r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo ', end='')
    if r1 == r2 == r3:
        print('equilátero!')
    elif r1 != r2 != r3 != r1:
        print('escaleno!')
    else:
        print('isósceles!')
else:
    print('Os segmentos acima não podem formar um triângulo!')
# O triângulo equilátero tem todos os lados iguais.
# O triângulo isósceles tem dois lados iguais.
# O triângulo escaleno tem todos os lados diferentes.
