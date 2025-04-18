#Verificar alistamento militar de acordo com a idade

from datetime import date
from time import sleep

ano = int(input('Digite o ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano

if idade < 18:
    print('Você ainda não tem idade para se alistar.')
    sleep(2)
    print(f'Faltam {18 - idade} anos para o seu alistamento.')
elif idade == 18:
    print('Você deve se alistar esse ano!')
    sleep(2)
    print('Procure o cartório militar mais próximo.')
elif idade > 18:
    print('Você já deveria ter se alistado.')
    sleep(2)
    print(f'Você já está atrasado {idade - 18} anos.')
    sleep(2)
    print('Procure o cartório militar mais próximo.')
else:
    print('Você não nasceu ainda!')
    sleep(2)
    print('Procure o cartório militar mais próximo quando completar 18 anos.') 
    sleep(2)
    print('Aguarde o seu nascimento.')
    
    