# Escreva um programa que receba duas listas e calcule a união dos elementos únicos dessas listas, usando conjuntos.

lista_um = ["Yonlu", "Suicide Song", "Mecânica Celeste Aplicada", True, 2024, 1.80]
lista_dois = ["Yonlu", "Suicide Song", "Mecânica Celeste Aplicada", 2023, False, 1.80, "Humiliation"]

lista_nova = set(lista_um).intersection(lista_dois)

print(lista_nova)