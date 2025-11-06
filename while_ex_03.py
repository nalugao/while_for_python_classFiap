#solciitar o nome e idade de N pessoas
# calcular a média de idade das pessoas

soma_idades = 0
conta_pessoas = 0

while True:
    nome = input('Inofrme o nome: ')
    if nome == "SAIR":
        break
    idade = int(input('Infome a idade: '))
    soma_idades += idade
    conta_pessoas += 1

media = soma_idades / conta_pessoas

print(f'A media de idade de pessoas é {media}')