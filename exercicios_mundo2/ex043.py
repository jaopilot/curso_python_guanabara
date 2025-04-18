#Calculadora de IMC
#IMC = peso / (altura * altura)

peso = float(input('Qual é o seu peso? '))
altura = float(input('Qual é a sua altura? '))
imc = peso / (altura ** 2)

print('O seu IMC é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está abaixo do peso ideal!')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal!')
elif 25 <= imc < 30:
    print('Você está com sobrepeso!')
elif 30 <= imc < 40:
    print('Você está com obesidade!')
elif imc >= 40:
    print('Você está com obesidade mórbida!')
else:
    print('Valor inválido!')
    