Dicionario1 = {
    'd1_id': 11,
    'd2_id': 33,
    'd3_id': 44,

}

Dicionario2 = {
    't1_id': 2,
    't2_id': 5,
    't3_id': 25,
}

Dicionario3 = {}

items_1 = Dicionario1.items()
items_2 = Dicionario1.items()

for item1,item2 in zip (items_1, items_2):
        Dicionario3[item1[0]] = item2[1]

print(Dicionario3)