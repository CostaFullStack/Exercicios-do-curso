# Crie uma função que aceita uma lista de strings e use a função reduce (importada de functools) para encontrar a maior string na lista.

from functools import reduce

def lista_string(*args):
    return reduce(lambda x,y: x if x > y else y, *args)

strings_lista = ['Lilya 4-ever', 'V for Vendetta', 'Black Swan', 'Perfect Blue', 'Akira']

print(f"""
Lista de strings: {strings_lista}
Maior string da lista: {lista_string(strings_lista)}
""")

