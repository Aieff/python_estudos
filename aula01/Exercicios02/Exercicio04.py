#Escreva um programa em python para dividir uma determinada lista em
#duas partes, onde o comprimento da primeira parte da lista é fornecida

comprimento = int(input("Digite o tamanho da primeira Lista"))

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

parte1 = lista[:comprimento]
parte2 = lista[comprimento:]

print("Parte 1: ",parte1)
print("Parte 2: ",parte2)