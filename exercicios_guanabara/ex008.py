print('+++++ Converta a medida X para km, hm, dam, dm, cm e mm +++++')

medida = float(input('Insira uma distancia em metros: '))

km = medida/1000
hm = medida/100
dam = medida/10
dm = medida*10
cm = medida*100
mm = medida*1000

print('A medida de {}m em KM corresponde a {:.2f}km'.format(medida, km))
print('A medida de {}m em HM corresponde a {:.2f}hm'.format(medida, hm))
print('A medida de {}m em DAM corresponde a {:.2f}dam'.format(medida,dam))
print('A medida de {}m em DM corresponde a {:.2f}dm'.format(medida,dm))
print('A medida de {}m em CM corresponde a {:.2f}cm'.format(medida,cm))
print('A medida de {}m em MM corresponde a {:.2f}mm'.format(medida, mm))

print('Exercicio concluido com sucesso!')
