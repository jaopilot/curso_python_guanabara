#Informar se foi reprovado de acordo com a média

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

print(f'A média entre {nota1} e {nota2} é igual a {media:.1f}')
if media < 5:
    print('O aluno está REPROVADO!')
elif media >= 5 and media < 7:  
    print('O aluno está de RECUPERAÇÃO!')
else:
    print('O aluno está APROVADO!')
# O aluno está reprovado se a média for menor que 5