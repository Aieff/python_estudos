# Faça um programa que mostre os números entre 2000 e 5000 (inclusive) que quando divididos por 12, produzam o resto igual a 5

for num in range(2000, 5000):
    if num % 12 == 5:
        print("Divididos por 12 que produzem resto igual a 5: ", num)
