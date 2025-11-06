# solciitar ao usuário 10 numeros e verificar de==se é par ou impar

cont = 0
conta_pares = 0

while cont < 10:
    numero = int(input('Informe um numero: '))
    if numero % 2 == 0:
        print("O número é PAR")
        conta_pares += 1
    else:
        print('O número é IMPAR')
    cont += 1

print(f'Quantidade de numeros pares: {conta_pares}')
print ('Fim do programa')