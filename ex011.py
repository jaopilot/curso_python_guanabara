largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

area = largura*altura
print('A área da parede é de: {:.2f}m²'.format(area))

latas = area/2

print('Serão necessárias {:.2f} latas de tinta para pintar uma parede de {}m². '.format(latas,area))

print('Exercicio concluido com sucesso!')