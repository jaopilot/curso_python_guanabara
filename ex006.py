#Digite o Dobro, Triplo e Raiz Quadrada de um numero.

n1 = int(input('Digite um número:'))

dobro = n1*2
triplo = n1*3
raiz = n1**(1/2)

print('O dobro de {} é: {}' .format(n1,dobro))
print('O triplo de {} é: {}' .format(n1,triplo))
print('A raiz quadrada de {} é: {:.2f}' .format(n1,raiz))

print('Exercicio concluido com sucesso!')