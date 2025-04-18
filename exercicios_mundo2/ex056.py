#Ler o nome, idade e sexo de 4 pessoas. No final, mostre:
#A média de idade do grupo
#O nome do homem mais velho
#Quantas mulheres têm menos de 20 anos

#Criando variáveis
soma_idade = 0
maior_idade = 0
maior_idade_homem = ''
cont_mulheres_menor_20 = 0
#Laço para repetir 4 vezes
for i in range(1, 5):
    print(f'----- {i}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    soma_idade += idade
    if sexo == 'M' and idade > maior_idade:
        maior_idade = idade
        maior_idade_homem = nome
    if sexo == 'F' and idade < 20:
        cont_mulheres_menor_20 += 1
#Cálculo da média de idade
media_idade = soma_idade / 4
#Exibindo os resultados
print(f'A média de idade do grupo é {media_idade} anos')
print(f'O homem mais velho tem {maior_idade} anos e se chama {maior_idade_homem}')
print(f'Ao todo são {cont_mulheres_menor_20} mulheres com menos de 20 anos')
#FIM
