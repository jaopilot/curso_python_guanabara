#Ler o sexo da pessoa enquanto os valores forem M ou F

while True:
    sexo = str(input('Informe seu sexo [M/F]: ')).upper()
    if sexo == 'M' or sexo == 'F':
            print(f'Sexo {sexo} registrado com sucesso!')
            
