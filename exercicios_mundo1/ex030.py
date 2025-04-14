numero = int(input('Digite um número inteiro: '))
if numero % 2 == 0:
    print('O número {} é par.'.format(numero))
else:
    print('O número {} é ímpar.'.format(numero))
# O código acima verifica se um número é par ou ímpar.
# O operador % (módulo) retorna o resto da divisão entre dois números.
# Se o resto da divisão do número por 2 for igual a 0, o número é par.
# Caso contrário, o número é ímpar.