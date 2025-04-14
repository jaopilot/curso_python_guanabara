# Ex23 - Desafio 23 - Separando dígitos de um número
numero = int(input('Digite um número entre 0 e 9999: '))

# Extraindo cada casa decimal
unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero // 100) % 10
milhar = (numero // 1000) % 10

# Exibindo os resultados
print(f'Analisando o número {numero}...')
print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')