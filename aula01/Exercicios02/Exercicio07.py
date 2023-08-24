Dicionario = {
    'valor1': 22,
    'valor2': 35,
    'valor3': 46,
    'valor4': 12,
    'valor5': 11,
    'valor6': 3,
    'valor7': 4,
}

total = 0

items = Dicionario.items()
for item in items:
    if(item[1] % 4 == 0):
        total += item[1]
print("O valor total é", total)