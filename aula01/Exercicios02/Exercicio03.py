#Escreva um programa que retorna verdadeiro se existir ao menos um elemento igual nas duas listas

lista_a = ["aba", "xyz", "ama", "abc", "aa", "a", "c"]
lista_b = ["abc", "321", "64", "dsa", "ffgdg", "a", "c"]


for elementos_a in lista_a:
    for elementos_b in lista_b:
        if elementos_a == elementos_b:
            print(elementos_a, True)