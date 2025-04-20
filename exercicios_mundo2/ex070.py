total_gasto = 0
produtos_acima_1000 = 0
produto_mais_barato = ''
preco_mais_barato = float('inf')

while True:
    print('-' * 30)
    print('CADASTRE UM PRODUTO')
    print('-' * 30)
    
    # Lê o nome do produto
    nome = input('Nome do produto: ').strip()
    
    # Lê o preço do produto
    while True:
        try:
            preco = float(input('Preço: R$'))
            break
        except ValueError:
            print('Por favor, insira um valor válido para o preço.')
    
    # Atualiza os valores
    total_gasto += preco
    if preco > 1000:
        produtos_acima_1000 += 1
    if preco < preco_mais_barato:
        preco_mais_barato = preco
        produto_mais_barato = nome
    
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
print(f'Total gasto na compra: R${total_gasto:.2f}')
print(f'Quantidade de produtos que custam mais de R$1000: {produtos_acima_1000}')
print(f'O produto mais barato foi "{produto_mais_barato}" que custa R${preco_mais_barato:.2f}')