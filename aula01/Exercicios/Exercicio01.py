# Escreva um programa que faça a soma de todos os números menores ou igual a 50 que são múltiplos de 3 ou 5.
# Utilize um laço do tipo while para realizar a tarefa.

total = 0
x = 1

while x <= 50:
    if x % 3 == 0 or x % 5 == 0:
        total += x
    x += 1

print("A soma dos números menores ou iguais a 50 que são múltiplos de 3 ou 5 é:", total)
