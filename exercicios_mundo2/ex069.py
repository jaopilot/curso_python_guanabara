total_maiores_18 = 0
total_homens = 0
total_mulheres_menos_20 = 0

while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    
    # Lê a idade
    while True:
        try:
            idade = int(input('Idade: '))
            break
        except ValueError:
            print('Por favor, insira um número válido para a idade.')
    
    # Lê o sexo
    while True:
        sexo = input('Sexo [M/F]: ').strip().upper()
        if sexo in ['M', 'F']:
            break
        print('Opção inválida! Digite apenas M ou F.')
    
    # Atualiza os contadores
    if idade > 18:
        total_maiores_18 += 1
    if sexo == 'M':
        total_homens += 1
    if sexo == 'F' and idade < 20:
        total_mulheres_menos_20 += 1
    
    # Pergunta se o usuário quer continuar
    while True:
        continuar = input('Quer continuar? [S/N]: ').strip().upper()
        if continuar in ['S', 'N']:
            break
        print('Opção inválida! Digite apenas S ou N.')
    
    if continuar == 'N':
        break

# Exibe os resultados
print('-' * 30)
print('RESULTADOS:')
print(f'Total de pessoas com mais de 18 anos: {total_maiores_18}')
print(f'Ao todo temos {total_homens} homens cadastrados.')
print(f'E temos {total_mulheres_menos_20} mulheres com menos de 20 anos.')