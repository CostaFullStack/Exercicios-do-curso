# Crie uma função que aceita uma lista de números e use a função map para retornar uma nova lista contendo o dobro de cada número na lista de entrada.

def lista_numeros(*args):
    return list(map(lambda x: x**2, *args))

numeros_lista = [1,2,3,4,5,6,7,8,9,10]

print(f"""
Lista de números: {numeros_lista}
Dobro da lista de números: {lista_numeros(numeros_lista)}
""")