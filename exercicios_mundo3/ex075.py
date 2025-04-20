# Lê quatro valores do teclado e armazena em uma tupla
numeros = (
    int(input("Digite o 1º número: ")),
    int(input("Digite o 2º número: ")),
    int(input("Digite o 3º número: ")),
    int(input("Digite o 4º número: "))
)

# Mostra a tupla
print(f"Você digitou os números: {numeros}")

# Quantas vezes apareceu o valor 9
print(f"O número 9 apareceu {numeros.count(9)} vez(es).")

# Em que posição foi digitado o primeiro valor 3
if 3 in numeros:
    print(f"O número 3 foi digitado na {numeros.index(3) + 1}ª posição.")
else:
    print("O número 3 não foi digitado.")

# Quais foram os números pares
pares = [n for n in numeros if n % 2 == 0]
print(f"Os números pares digitados foram: {pares if pares else 'Nenhum número par foi digitado.'}")