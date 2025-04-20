# Tupla com os produtos e seus respectivos preços
produtos = (
    'Pão', 1.50,
    'Leite', 3.20,
    'Café', 8.50,
    'Arroz', 12.30,
    'Feijão', 9.80,
    'Açúcar', 4.50,
    'Óleo', 7.90,
    'Manteiga', 5.60
)

# Cabeçalho da tabela
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)

# Exibição dos produtos e preços
for i in range(0, len(produtos), 2):
    nome = produtos[i]
    preco = produtos[i + 1]
    print(f'{nome:<30} R$ {preco:>7.2f}')

# Rodapé da tabela
print('-' * 40)