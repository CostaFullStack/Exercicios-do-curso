# Dado as listas: 
# lista_um = [10,6,8,15,29,33,4,11,50]
# lista_dois = [41,25,4,29,1,63,15]
# Mostre na tela a soma dos números contidos nas duas listas ao mesmo tempo (use set para ajudar na interseção).

lista_um = [10,6,8,15,29,33,4,11,50]
lista_dois = [41,25,4,29,1,63,15]

conjunto_novo = set(lista_um).intersection(lista_dois)

soma = 0

for conjunto_da_vez in conjunto_novo:
    soma += conjunto_da_vez

print(f"A soma dos números contidos na lista ao mesmo tempo é de: {soma}")