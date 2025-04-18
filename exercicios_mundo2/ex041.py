#Categoria de acordo com a idade

from time import sleep

ano_de_nascimento = int(input('Ano de nascimento: '))
ano_atual = int(input('Digite o ano atual: '))
idade = ano_atual - ano_de_nascimento
sleep(1)
print('Calculando sua idade...')
sleep(1)
print(f'Você tem {idade} anos.')

if idade <= 9:
    print('Você é um atleta mirim.')
elif idade <= 14:
    print('Você é um atleta infantil.')
elif idade <= 19:
    print('Você é um atleta junior.')
elif idade <= 20:
    print('Você é um atleta sênior.')
else:
    print('Você é um atleta master.')
#O código acima calcula a idade de um atleta com base no ano de nascimento e no ano atual.