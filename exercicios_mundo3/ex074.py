from random import randint

# Gerar cinco números aleatórios e colocá-los em uma tupla
numeros = (randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))

# Mostrar os números gerados
print('Os números sorteados foram:', numeros)

# Indicar o menor e o maior valor
print(f'O menor valor sorteado foi: {min(numeros)}')
print(f'O maior valor sorteado foi: {max(numeros)}')