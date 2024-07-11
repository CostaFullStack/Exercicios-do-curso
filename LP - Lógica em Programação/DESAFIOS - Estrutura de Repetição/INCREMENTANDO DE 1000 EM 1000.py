# Escreva um programa que declare um inteiro, inicialize-o com 0, e incremente-o de 1000 em 1000, imprimindo seu valor na tela, até que seu valor seja 100000 (cem mil).

# com for
inicio = 0

for i in range(100000):
    if inicio == i:
        inicio += 1000
        print(inicio)
        
# com while
inicio = 0

while inicio < 100000:
    inicio += 1000
    print(inicio)


