#Criar tabuada de acordo com o numero que o usuario digitar

numero = int(input('Digite um numero para ver sua tabuada: '))
print(f'--- A tabuada do {numero} é: ---')

for i in range(1, 11):
    print(f'{numero} x {i} = {numero * i}')
print('FIM')  
