#Exemplo da aula

lista_a = [1, 2, 3, 4, 5]
lista_b = [4, 5, 6, 7, 8]

for valor_a in lista_a:
    for valor_b in lista_b:
        if valor_a == valor_b:
            print('Valor idêntico de ambas as listas', valor_a)