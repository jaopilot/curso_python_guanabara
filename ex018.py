# Uso da biblioteca math.
# math.radians converte para radianos.

import math
angulo = float(input('Digite o valor do angulo: '))

seno = math.sin(math.radians((angulo)))
cosseno = math.cos(math.radians((angulo)))
tangente = math.tan(math.radians((angulo)))

print('O seno de {}º é: {:.2f}'.format(angulo, seno))
print('O cosseno de {}º é: {:.2f}'.format(angulo, cosseno))
print('A tangente de {}º é: {:.2f}'.format(angulo, tangente))