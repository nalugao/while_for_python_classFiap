#solciitar as notas de 10 alunos.
#exibir a mior e a menor nota.
#exibir o nome do aluno que obteve a maior nota

maior_nota = 0 
nome_maior_nota = ""

menor_nota = 10
nome_menor_nota = ""

for cont in range(5):
    nome = input('ALuno: ')
    nota = float(input('Nota: '))
    if nota > maior_nota:
        maior_nota = nota
        nome_maior_nota = nome
    if nota < menor_nota:
        menor_nota = nota
        nome_menor_nota = nome

print(f'Maior nota: {maior_nota} do aluno {nome_maior_nota}')
print(f'Menor nota: {menor_nota} do aluno {nome_menor_nota}')