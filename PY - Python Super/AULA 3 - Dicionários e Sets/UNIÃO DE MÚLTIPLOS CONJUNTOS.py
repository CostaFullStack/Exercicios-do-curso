#  Crie um programa que realize a união de múltiplos conjuntos e exiba o conjunto resultante.

conjunto_um = {'Lilya 4-ever', 2002, 'Drama'}
conjunto_dois = {'Black Swan', 2010, 'Thriller e Drama'}
conjunto_tres = {'Cuando Acecha La Maldad', 2023, 'Thriller e Horror'}

uniao_conjuntos = conjunto_um.union(conjunto_dois, conjunto_tres)

print(f"União dos conjuntos: {uniao_conjuntos}")