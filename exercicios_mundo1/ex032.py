ano = int(input('Digite o ano que você quer analisar: '))
if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')
# O ano é bissexto se for divisível por 4, mas não por 100, exceto se for divisível por 400.
# Exemplo: 2000 é bissexto, 1900 não é bissexto, 2004 é bissexto, 2001 não é bissexto.
# O ano 2000 é bissexto, pois é divisível por 4 e 400.
# O ano 1900 não é bissexto, pois é divisível por 4, mas não por 400.