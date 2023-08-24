#Escreva um programa para contar o número de elementos de tamanho 2 ou mais de uma lista qualquer, onde o
#primeiro e o último caractere do elemento são os mesmo

lista = ["aba", "xyz", "ama", "abc", "aa", "a", "c"]
count = 0

for elemento in lista:
    if len(elemento) >= 2 and elemento[0] == elemento[-1]:
        count += 1

print("Número de elementos com primeiro e último caractere iguais:", count)
