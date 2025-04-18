#Ler um numero qualquer e mostrar o seu fatorial

from math import factorial
from time import sleep

num1 = int(input('Digite um número para calcular o seu fatorial: '))
print('Calculando o fatorial de {}!'.format(num1))
sleep(2)
print('O fatorial de {}! é igual a {}.'.format(num1, factorial(num1)))
print('FIM')
