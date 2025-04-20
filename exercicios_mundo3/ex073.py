# Tupla com os 20 primeiros colocados do Campeonato Brasileiro
times_brasileirao = (
    'Botafogo', 'Palmeiras', 'Flamengo', 'Atlético-MG', 'Fluminense',
    'Grêmio', 'Athletico-PR', 'São Paulo', 'Internacional', 'Fortaleza',
    'Cruzeiro', 'Bragantino', 'Corinthians', 'Cuiabá', 'Bahia',
    'Goiás', 'Santos', 'Vasco', 'América-MG', 'Coritiba'
)

# a) Os 5 primeiros colocados
print('Os 5 primeiros colocados são:')
print(times_brasileirao[:5])

# b) Os últimos 4 colocados
print('\nOs 4 últimos colocados são:')
print(times_brasileirao[-4:])

# c) Times em ordem alfabética
print('\nTimes em ordem alfabética:')
print(sorted(times_brasileirao))

# d) Posição do Fluminense na tabela
posicao_fluminense = times_brasileirao.index('Fluminense') + 1
print(f'\nO Fluminense está na {posicao_fluminense}ª posição.')