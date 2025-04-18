#Ler varios numeros inteiros do teclado, só para quando o usuario digita 999.

while True:
    n = int(input('Digite um numero [999 para parar]: '))
    if n == 999:
        break
    print(f'Voce digitou {n}')
print('Fim do programa!')
