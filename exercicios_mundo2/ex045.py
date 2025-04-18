#Jokenpô

from random import choice
from time import sleep

print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
itens = ('Pedra', 'Papel', 'Tesoura')
computador = choice(itens)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('-=' * 11)
print(f'O computador jogou {computador}')
print(f'O jogador jogou {itens[jogador]}')
print('-=' * 11)

if computador == itens[jogador]:
    print('Empate!')
elif (computador == 'Pedra' and itens[jogador] == 'Tesoura') or (computador == 'Papel' and itens[jogador] == 'Pedra') or (computador == 'Tesoura' and itens[jogador] == 'Papel'):
    print('Computador Venceu!')
else:
    print('Jogador Venceu!')    
print('-=' * 11)
print('Fim do jogo!')
