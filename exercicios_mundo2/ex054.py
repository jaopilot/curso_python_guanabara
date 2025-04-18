#Ler o ano de nascimento de 7 pessoas e contar quantas são maiores de idade

ano_atual = int(input('Digite o ano atual: '))
menor_idade = 0
maior_idade = 0

for i in range(7):
    ano_nascimento = int(input('Digite o ano de nascimento: '))
    idade = ano_atual - ano_nascimento
    if idade >= 18:
        print('Maior de idade')
        maior_idade += 1
    else:
        print('Menor de idade')
        menor_idade += 1
        
print(f'Total de pessoas maiores de idade: {maior_idade}')
print(f'Total de pessoas menores de idade: {menor_idade}')