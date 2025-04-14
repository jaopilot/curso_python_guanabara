nome = str(input('Digite seu nome completo: '))
nome = nome.lower()
# Transformando o nome em letras minúsculas
nome_separado = nome.split()
print(nome_separado)

if 'silva' in nome_separado:
    print('Seu nome tem Silva!')
else:
    print('Seu nome não tem Silva!')
# Verificando se 'silva' está na lista de nomes

