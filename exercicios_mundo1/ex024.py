#Recebe o nome da cidade
cidade = str(input('Em qual cidade você nasceu? ')).split()

# Verifica se a cidade começa com 'Santo'
if cidade[0].lower() == 'santo':
    print('A cidade começa com Santo!')
else:
    print('A cidade não começa com Santo!')
    
    