
soma = 0
# Para cada número ímpar de 1 a 500, se o número for divisível por 3, somar
for c in range(0,500,3):
    if c % 3 == 0:
        soma = soma + c
print(f'A soma de todos os números ímpares de 1 a 500 que são divisíveis por 3 é {soma}.')
      