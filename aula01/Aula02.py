#Indique se o triângulo é Equilátero, Isósceles, Escaleno3

def verificar_triangulo(lado_a, lado_b, lado_c):
    if lado_a <= 0 or lado_b <= 0 or lado_c <= 0:
        return "Valores inválidos. Os lados devem ser números positivos maiores que zero."
    elif lado_a + lado_b <= lado_c or lado_a + lado_c <= lado_b or lado_b + lado_c <= lado_a:
        return "Não é possível formar um triângulo com esses lados."
    elif lado_a == lado_b and lado_b == lado_c:
        return "Triângulo Equilátero"
    elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
        return "Triângulo Isósceles"
    else:
        return "Triângulo Escaleno"

# Solicitar os lados do usuário
lado_a = float(input("Digite o valor do primeiro lado: "))
lado_b = float(input("Digite o valor do segundo lado: "))
lado_c = float(input("Digite o valor do terceiro lado: "))

resultado = verificar_triangulo(lado_a, lado_b, lado_c)
print(resultado)