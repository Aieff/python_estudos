#Escreva um programa que remova valores duplicados de uma lista e exiba
#o antes e o depois.

lista_duplicados = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]

print("Antes:", lista_duplicados)

lista = []

for item in lista_duplicados:
    if item not in lista:
        lista.append(item)

lista_duplicados[:] = lista

print("Depois:", lista_duplicados)
