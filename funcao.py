def print_livro(nome_livro, nome_autor):
    print(f"Nome do livro: {nome_livro}")
    print(f"Nome do autor: {nome_autor}")

print_livro("1984", "Geroge")

# Faça um função para calcular o IMC de uma pessoa 
# IMC = PESO/(altura^2)

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

def calcula_imc(peso, altura):
    imc = peso/(altura * altura)
    print(imc)

calcula_imc(peso, altura)