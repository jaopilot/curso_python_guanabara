import random
numero = int(input('Digite um número inteiro, entre 1 e 5: '))
numeropensado = random.randint(1, 5)
if numero == numeropensado:
    print('Você acertou!')
else:
    print('Você errou! O número pensado era {}.'.format(numeropensado))
# O código acima pede um número inteiro entre 1 e 5 e compara com um número pensado aleatoriamente. Se o usuário acertar, imprime "Você acertou!", caso contrário, imprime "Você errou!" e mostra o número pensado