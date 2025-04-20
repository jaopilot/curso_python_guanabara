# Jogo de Par ou Ímpar
from random import randint

print('=-' * 15)
print('Vamos jogar PAR ou ÍMPAR!')
print('=-' * 15)

vitorias = 0

while True:
    jogador = int(input('Digite um valor: '))
    escolha = ''
    while escolha not in 'PI':
        escolha = input('Par ou Ímpar? [P/I] ').strip().upper()[0]
    
    computador = randint(0, 10)
    total = jogador + computador
    resultado = 'PAR' if total % 2 == 0 else 'ÍMPAR'
    
    print('-' * 30)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} deu {resultado}.')
    print('-' * 30)
    
    if (escolha == 'P' and resultado == 'PAR') or (escolha == 'I' and resultado == 'ÍMPAR'):
        print('Você VENCEU!')
        vitorias += 1
        print('Vamos jogar novamente...')
        print('=-' * 15)
    else:
        print('Você PERDEU!')
        break

print('=-' * 15)
print(f'GAME OVER! Você venceu {vitorias} vez(es).')