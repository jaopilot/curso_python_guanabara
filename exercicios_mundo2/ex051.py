#Mostrar os 10 primeiros termos de uma PA

print('10 TERMOS DE UMA PA')
print('-=' * 10)    
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

for i in range(10):
    print(primeiro_termo, end=' -> ')
    primeiro_termo += razao
print('ACABOU')
print('-=' * 10)
