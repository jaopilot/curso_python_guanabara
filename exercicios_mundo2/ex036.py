valor_da_casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o seu salário? R$ '))
tempo = int(input('Em quantos anos você pretende pagar? '))
porcentagem_comprometida = float(input('Qual a porcentagem do salário que você quer comprometer? '))

prestacao = valor_da_casa / (tempo * 12)
porcentagem = salario * porcentagem_comprometida / 100
print(f'O valor da casa é de R$ {valor_da_casa:.2f}')

print(f'A prestação mensal será de R$ {prestacao:.2f}')
print(f'A porcentagem do salário é de R$ {porcentagem:.2f}')

if prestacao <= porcentagem:
    print('Empréstimo aprovado!')
else:
    print('Empréstimo negado!')
