print('-' * 30)
print('CAIXA ELETRÔNICO')
print('-' * 30)

# Solicita o valor a ser sacado
while True:
    try:
        valor = int(input('Qual valor você quer sacar? R$'))
        if valor > 0:
            break
        else:
            print('Por favor, insira um valor positivo.')
    except ValueError:
        print('Por favor, insira um valor válido.')

# Inicializa as cédulas disponíveis
cedulas = [50, 20, 10, 1]
quantidades = {}

# Calcula a quantidade de cédulas de cada valor
for cedula in cedulas:
    quantidades[cedula] = valor // cedula
    valor %= cedula

# Exibe o resultado
print('-' * 30)
print('CÉDULAS ENTREGUES:')
for cedula, quantidade in quantidades.items():
    if quantidade > 0:
        print(f'{quantidade} cédula(s) de R${cedula}')
print('-' * 30)