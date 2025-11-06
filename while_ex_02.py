#solicitar o nome e a idade de N pessoas -- aqui temos controle de informações
#contar quantas pessoas são menores de idade

# quantidade = int(input('Informe a quantidade de pessoas: '))

# cont = 0
# conta_menores = 0

# while cont < quantidade:
#     nome = input('Informe o nome: ')
#     idade = int(input('Informe a idade: '))
#     if idade < 18:
#         conta_menores += 1
#     cont += 1

# print(f'Quantidade de pessoas menores de idade {conta_menores}')

conta_menores = 0
conta_maiores = 0

while True: #loop infinito
    nome = input('Informe o nome (digite SAIR para finalizar): ')
    if nome == "SAIR":
        break
    idade = int(input('Informe a idade: '))
    if idade < 18:
        conta_menores += 1
    else:
        conta_maiores +=1

print(f'Quantidade de pessoas menores de idade {conta_menores}')
print(f'Quantidade de pessoas maiores de idade {conta_maiores}')
