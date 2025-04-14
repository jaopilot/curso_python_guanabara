salario = float(input('Qual é o salário do funcionário? R$'))
if salario <= 1250:
    aumento = salario * 0.15
else:
    aumento = salario * 0.10
novo_salario = salario + aumento
print(f'O funcionário que ganhava R${salario:.2f} agora passa a receber R${novo_salario:.2f} com o aumento de R${aumento:.2f}.')
# O código calcula o novo salário de um funcionário com base no salário atual e na porcentagem de aumento.
# Se o salário for menor ou igual a R$1250, o aumento é de 15%.
# Caso contrário, o aumento é de 10%. O novo salário e o valor do aumento são exibidos formatados com duas casas decimais.
# O código utiliza a função input() para receber o salário do funcionário e a função print() para exibir o resultado.