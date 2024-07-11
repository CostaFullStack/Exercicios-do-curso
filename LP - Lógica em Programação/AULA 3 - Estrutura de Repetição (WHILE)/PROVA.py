# Escreva um programa em python que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite 0 (zero). No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética.

contagem = 0
media = 0
soma = 0 

while True:
    numero = int(input("Digite um número inteiro ou 0 para sair: "))
    # ignorando o número 0 na contagem
    if numero == 0:
        break
    else:
        contagem += 1
        soma += numero
        media = (soma / contagem)

print(f"""
Programa encerrado!
Números digitados: {contagem}
Soma: {soma}
Média: {media:.1f}
""")

# forma mais robusta
contagem = 0
media = 0
soma = 0 
numero_maior_zero = False

while True:
    numero = int(input("Digite um número inteiro ou 0 para sair: "))
    if numero == 0:
        # ignorando o número 0 na contagem
        if numero_maior_zero:
            break
        # se o usuário digitar 0 na primeira vez
        else:
            print("Nenhum número acima de zero foi digitado!")
            break
    # caso o usuário digite um número maior que 0
    else:
        numero_maior_zero = True
        contagem += 1
        soma += numero
        media = (soma / contagem)

if numero_maior_zero:
    print(f"""
Programa encerrado!
Números digitados: {contagem}
Soma: {soma}
Média: {media:.1f}
""")