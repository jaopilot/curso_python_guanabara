nome = str(input('Qual é o seu nome? '))
print('Prazer em te conhecer, {}!'.format(nome))
# O código acima pede o nome do usuário e imprime uma mensagem de boas-vindas.
print('O seu primeiro nome é {}.'.format(nome.split()[0]))
# O código acima divide o nome em partes e imprime o primeiro nome.
print('Seu sobrenome é {}.'.format(nome.split()[-1]))
# O código acima divide o nome em partes e imprime o último sobrenome.

