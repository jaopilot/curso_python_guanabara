# Definindo a tupla com várias palavras
palavras = ('python', 'programacao', 'curso', 'guanabara', 'estudo', 'desenvolvimento')

# Iterando sobre cada palavra na tupla
for palavra in palavras:
    print(f'\nNa palavra "{palavra.upper()}" temos as vogais: ', end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end=' ')