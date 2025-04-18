import random

numero_pensado = random.randint(0, 10)
numero_de_tentativas = 0
print('Vou pensar em um número entre 0 e 10. Tente adivinhar!')

while True:
    palpite = int(input('Qual é o seu palpite? '))
    if palpite < numero_pensado:
        numero_de_tentativas = numero_de_tentativas + 1
        print('Mais...')
    elif palpite > numero_pensado:
        numero_de_tentativas = numero_de_tentativas + 1
        print('Menos...')
    else:
        print(f'Parabéns! Você acertou o número {numero_pensado}!')
        print(f'Você precisou de {numero_de_tentativas} tentativas.')
        break
    print('Tente novamente!')