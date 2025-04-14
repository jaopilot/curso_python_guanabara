frase = str(input('Digite uma frase: '))
frase = frase.lower()

print(frase)

print('Essa frase tem {} letras A'.format(frase.count('a')))
print('A primeira letra A aparece na posição {}'.format(frase.find('a') + 1))
print('A última letra A aparece na posição {}'.format(frase.rfind('a') + 1))

# A função find() retorna a posição da primeira ocorrência do caractere
# A função rfind() retorna a posição da última ocorrência do caractere
# A função count() retorna a quantidade de ocorrências do caractere