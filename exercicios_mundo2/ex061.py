#Refazer o exercicio 51, utilizando while

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

while primeiro_termo <= 10:
    print(primeiro_termo, end=' -> ')
    primeiro_termo += razao
print('FIM')
