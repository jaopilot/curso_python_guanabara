#Ler o peso de cinco pessoas e informar o maior e o menor peso lido.

maior_peso = 0
menor_peso = 0 

for i in range(1, 6):
    peso = float(input(f'Peso da {i}ª pessoa: '))
    
    if i == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso

print(f'O maior peso lido foi {maior_peso}kg')
print(f'O menor peso lido foi {menor_peso}kg')
