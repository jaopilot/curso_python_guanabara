velocidade = int(input('Qual é a velocidade do carro? '))
if velocidade > 80:
    print('Você foi multado!')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
else:
    print('Você está dentro do limite de velocidade.')
# O código acima verifica a velocidade de um carro e calcula a multa se a velocidade ultrapassar 80 km/h.
# A multa é de R$7,00 para cada km/h acima do limite.