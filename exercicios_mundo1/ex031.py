distancia = float(input('Qual a distância da sua viagem? '))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('Você está prestes a começar uma viagem de {}Km.'.format(distancia))
print('E o preço da sua passagem será de R${:.2f}'.format(preco))
print('Tenha uma boa viagem!')
# O código acima calcula o preço de uma passagem de acordo com a distância da viagem.
# Se a distância for menor ou igual a 200 km, o preço é R$0,50 por km.
# Se a distância for maior que 200 km, o preço é R$0,45 por km.
# O preço total é calculado multiplicando a distância pelo preço por km.