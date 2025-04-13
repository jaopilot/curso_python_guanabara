print('++++ Conversor de moedas ++++')

v1 = float(input('Digite o valor que você tem em carteira: '))
dolar = float(input('Digite a cotação atual do dolar: '))
resultado = v1/dolar

print('Com R${}, você poderá comprar US${:.2f}'.format(v1,resultado))

print('Exercicio concluido com sucesso!')