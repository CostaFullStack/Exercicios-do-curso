# Crie uma função chamada criar_lista_de_compras que aceita um número variável de itens de compras como argumentos posicionais (usando *args). A função deve criar e retornar uma lista de compras que contenha todos os itens fornecidos.

def criar_lista_de_compras(*args):
    lista_compras = []
    for i in args:
        lista_compras.append(i)

    return lista_compras

print(f"""
Lista de números: {criar_lista_de_compras(20,30,40,50,10)}
Lista de strings: {(criar_lista_de_compras('Laranja','Pera','Maçã','Uva','Banana nanica'))}
""")
