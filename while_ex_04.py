#calculadora

while True: 
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Sair')

    opcao = int(input('Escolha uma opção: '))


    if 1 <= opcao <= 4:
        a = float(input('Informe um numero: '))
        b = float(input('Informe um numero: '))

    if opcao == 1:
        print(f'Soma: {a + b}')

    elif opcao == 2:
        print(f'Subtração: {a - b}')

    elif opcao == 3:
        print(f'Multiplicação: {a * b}')

    elif opcao == 4:
        if b != 0:
            print(f'Divisão: {a / b}')
        else:
            print("ERRO: Não é possível realizar uma divisão por zero")

    elif opcao == 5:
        break

    else:
        print('Opção inválida')