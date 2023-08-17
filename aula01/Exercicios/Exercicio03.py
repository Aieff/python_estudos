# Escreva um programa que leia do usuário um número inteiro,
# maior que 1 e imprime o enésimo número da sequencia de fibonacci


numero = int(input(print("Digite um número: ")))

if (numero <= 1):
    print("Digite um número inteiro maior que 1!")
else:
    n1 = 0
    n2 = 1

    termo = numero

    for i in range (0,termo):
        f_final = n1 + n2
        n1 = n2
        n2 = f_final
    print(f"Seu enésimo número da sequencia de fibonacci é: {f_final}")
