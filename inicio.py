import math

custo_encomenda = 10
custo_posse = 0.70
prazo_entrega = 7

procura_anual = 50000

tecido_s = 1000
algodao_s = 1000
fio_s = 1000
poliester_s = 1000

tecido = 2200
algodao = 2200
fio = 2200
poliester = 2200

quantidade_eco_encomenda = math.sqrt((2*procura_anual*custo_encomenda)/custo_posse)
procura_diaria = procura_anual/365

my_dict = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}

tecido_por_tipo = {
    'Tshirt' : 1.00,
    'Calcoes' : 0.80,
    'Camisola' : 0.50,
    'Calcas' : 1.20
}
algodao_por_tipo = {
    'Tshirt' : 0.80,
    'Calcoes' : 0.70,
    'Camisola' : 0.35,
    'Calcas' : 0.95
}
fio_por_tipo = {
    'Tshirt' : 0.40,
    'Calcoes' : 0.40,
    'Camisola' : 0.50,
    'Calcas' : 0.35
}
poliester_por_tipo = {
    'Tshirt' : 1.30,
    'Calcoes' : 1.40,
    'Camisola' : 1.15,
    'Calcas' : 1.50
}

razao_tamanho = {
    'XS' : 0.50,
    'S' : 0.75,
    'M' : 1.00,
    'L' : 1.5,
    'XL' : 2.00
}

preco_por_metro = {
    'Tecido' : 7.00,
    'Algodao' : 5.50,
    'Fio' : 4.50,
    'Poliester' : 10.00
}