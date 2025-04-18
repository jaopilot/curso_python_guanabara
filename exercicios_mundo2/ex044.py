#Calcular valor a ser pago por um produto, considerando o preço normal e a condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros
print('=-' * 20)

print('LOJAS RODRIGUES')
print('=-' * 20)

preco = float(input('Preço das compras: R$ '))
print('=-' * 20)
print('FORMAS DE PAGAMENTO')
print('''[ 1 ] À vista dinheiro/cheque
[ 2 ] À vista no cartão
[ 3 ] Em até 2x no cartão
[ 4 ] 3x ou mais no cartão''')
print('=-' * 20)
opção = int(input('Qual é a opção? '))
print('=-' * 20)

if opção == 1:
    total = preco - (preco * 10 / 100)
    print('A sua compra de {:.2f} vai custar {:.2f} no final.'.format(preco, total))
elif opção == 2:
    total = preco - (preco * 5 / 100)
    print('A sua compra de {:.2f} vai custar {:.2f} no final.'.format(preco, total))
elif opção == 3:
    total = preco
    print('A sua compra de {:.2f} vai custar {:.2f} no final.'.format(preco, total))
elif opção == 4:
    total = preco + (preco * 20 / 100)
    parcelas = int(input('Quantas parcelas? '))
    parcela = total / parcelas
    print('A sua compra de {:.2f} vai custar {:.2f} no final.'.format(preco, total))
    print('Sua compra será parcelada em {}x de {:.2f} com juros.'.format(parcelas, parcela))
else:
    print('Opção inválida. Tente novamente!')
print('=-' * 20)
print('Volte sempre à LOJAS RODRIGUES!')
print('=-' * 20)
#Fim do programa
