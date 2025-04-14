nome_completo = str(input('Digite seu nome completo: '))

print('O seu nome em maisculas é: {}' .format(nome_completo.upper()))
print('O seu nome em minusculas é: {}' .format(nome_completo.lower()))
print('Seu nome tem ao todo: {} letras' .format(len(nome_completo) - nome_completo.count(' ')))  # Total de letras
nome_separado = nome_completo.split()  # Separa o nome em partes
print('Seu primeiro nome é {} e ele tem {} letras' .format(nome_separado[0], len(nome_separado[0])))  # Primeiro nome