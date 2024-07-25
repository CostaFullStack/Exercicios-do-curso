# Crie uma função que aceita uma lista de números e use a função filter para retornar uma nova lista contendo apenas os números pares da lista de entrada.

def lista_numeros(*args):
    return list(filter(lambda x: x % 2 == 0, *args))

numeros_lista = [1,2,3,4,5,6,7,8,9,10]

print(f"""
Lista de números: {numeros_lista}
Pares da lista de números: {lista_numeros(numeros_lista)}
""")