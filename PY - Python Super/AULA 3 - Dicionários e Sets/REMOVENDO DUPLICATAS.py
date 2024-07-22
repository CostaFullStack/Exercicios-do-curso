# Crie um programa que receba uma lista de números e remova todas as duplicatas usando um conjunto (set). Em seguida, exiba a lista original e a lista sem duplicatas.

lista = [1,2,2,3,3,4,4,5,5,6,7,8,9,11]
conjunto = set()

conjunto.update(lista)

print(f"Lista original: {lista}")
print(f"Lista sem duplicatas: {list(conjunto)}")