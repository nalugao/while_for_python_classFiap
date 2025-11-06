for cont in range(10):      #0,1,2,3,4,5,6,7,8,9
    print(cont)

# é o mesmo que:
# cont = 0
# while cont < 10:
#     print(cont)
#     cont += 1

#se eu nao quiser começar em 0:

for cont in range(5, 10):      #5,6,7,8,9
    print(cont)

#começa em 5 e até 10 aumenta de 2 em dois:

for cont in range(5, 10, 2):      #5,7,9
    print(cont)

#exibir os numeros impares de 1 a 49:

for cont in range(1, 50, 2):
    print(cont)

#exibir os numeros pares de 1 a 49:

for cont in range(2, 50, 2):
    print(cont)