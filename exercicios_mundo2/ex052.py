#Ler o numero e dizer se ele é primo ou não

numero = int(input('Digite um número: '))
cont = 0
for i in range(1, numero + 1):
    if numero % i == 0:
        cont += 1
        print(f'\033[33m{i}\033[m', end=' ')
    else:
        print(f'\033[31m{i}\033[m', end=' ')
if cont == 2:
    print(f'\nO número {numero} é \033[32mPRIMO\033[m!')
else:
    print(f'\nO número {numero} \033[31mnão é PRIMO\033[m!')
print(f'Ele foi divisível {cont} vezes.')
print('FIM')
print('=-' * 20)

