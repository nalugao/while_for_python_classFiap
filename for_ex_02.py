#solciitar o nome e a idade de 10 pessoas
#contar a quantidade de pessoas menores de idades

# conta_menores = 0

# quantidade = int(input('Qauntidade de pessoas: '))

# for cont in range(10):
#     nome = input('Nome: ')
#     idade = int(input('Idade: '))
#     if idade < 18:
#         conta_menores += 1

# print(f'Quantidade de pessoas menores de idade: {conta_menores}')


conta_menores = 0

quantidade = int(input('Qauntidade de pessoas: '))

for cont in range(quantidade):
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    if idade < 18:
        conta_menores += 1

print(f'Quantidade de pessoas menores de idade: {conta_menores}')