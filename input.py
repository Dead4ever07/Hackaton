import re

with open('encomenda3.txt', 'r') as file:
    lines = file.readlines()

items = []
for line in lines:
    parts = line.split()
    if len(parts) == 3:  
        num = parts[0]  
        item = parts[1] 
        tamanho = parts[2]  
        items.append((num, item, tamanho))
    elif len(parts) == 1:
        padrao = r'(\d+)(Camisola|Tshirt|Calcoes|Calcas)([LXS]{1,2})'
        conjuntos = re.findall(padrao, line.strip())
        for c in conjuntos:
            num = c[0]  
            item = c[1] 
            tamanho = c[2]  
            items.append((num, item, tamanho))
    else:
        padrao= r'(\d+)\s+(Camisola|Tshirt|Calcoes|Calcas)\s+do\s+tamanho\s+([LXS]{1,2})'
        conjuntos = re.findall(padrao, line)
        for c in conjuntos:
            num = c[0]
            item = c[1]
            tamanho = c[2]
            items.append((num, item, tamanho))



for num, item, tamanho in items:
    print(f'Num: {num}, Item: {item}, Tamanho: {tamanho}')