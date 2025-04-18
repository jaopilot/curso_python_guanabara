#Ler dois valores na tela e abrir um menu de opções:

valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))

while True:
    print('''Escolha uma opção:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do Programa''')
    
    opcao = int(input('Qual é a sua opção? '))

    if opcao == 1:
        soma = valor1 + valor2
        print(f'A soma entre {valor1} e {valor2} é {soma}.')
    elif opcao == 2:
        multiplicacao = valor1 * valor2
        print(f'A multiplicação entre {valor1} e {valor2} é {multiplicacao}.')
    elif opcao == 3:
        maior = max(valor1, valor2)
        print(f'O maior número entre {valor1} e {valor2} é {maior}.')
    elif opcao == 4:
        valor1 = int(input('Digite o primeiro valor: '))
        valor2 = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('Saindo do programa... Até logo!')
        break
    else:
        print('Opção inválida! Tente novamente.')