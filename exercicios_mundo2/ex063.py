# Sequência de Fibonacci
# Crie um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.

while True:
    try:
        n = int(input('Quantos termos você quer mostrar? '))
        if n <= 0:
            print('Por favor, digite um número inteiro positivo.')
            continue
        break
    except ValueError:
        print('Por favor, digite um número inteiro.')

# Inicializando os dois primeiros termos da sequência
t1, t2 = 0, 1
print('~' * 30)
print(f'{t1} → {t2}', end='')

# Gerando os próximos termos
for _ in range(3, n + 1):
    t3 = t1 + t2
    print(f' → {t3}', end='')
    t1, t2 = t2, t3

print(' → FIM')
print('~' * 30)