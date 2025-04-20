#Ler varios numeros um de cada vez e mostrar a tabuada até digitar um numero negativo

while True:
    n = int(input('Digite um numero para ver sua tabuada (negativo para parar): '))
    if n < 0:
        break
    print('-' * 12)
    for i in range(1, 11):
        print(f'{n} x {i:2} = {n * i}')
    print('-' * 12)
print('Programa encerrado!')
#FIM