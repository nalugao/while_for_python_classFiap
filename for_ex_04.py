#solciitar as notas de 10 alunos
#armazenar todas as notas em uma lista

lista_notas = []
lista_nomes = []

for cont in range(3):
    nome = input('Nome: ')
    lista_nomes.append(nome)
    nota = float(input('Nota: '))
    lista_notas.append(nota)

#percorre os indices da lsita utilizando os dados
for indice in range(3):
    print(f'{lista_nomes[indice]} - {lista_notas[indice]}')


print(lista_nomes)
print(lista_notas)

print(lista_nomes[0])
print(lista_notas[0])