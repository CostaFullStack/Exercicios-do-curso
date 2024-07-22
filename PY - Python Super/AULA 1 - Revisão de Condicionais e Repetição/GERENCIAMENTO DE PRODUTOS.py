# Você foi contratado para desenvolver um programa simples para auxiliar em um processo de compra de produtos. O programa deve permitir ao usuário inserir o nome e o preço de vários produtos, perguntando se deseja continuar inserindo mais produtos após cada entrada. Ao final, o programa deve fornecer um resumo da compra, incluindo:
# A) O total gasto na compra.
# B) A quantidade de produtos que custam mais de R$1000.
# C) O nome do produto mais barato.
# Desenvolva o programa em Python, utilizando conceitos de entrada/saída de dados, condicionais e laços de repetição.

soma = 0
contagem = 0
preco_mais_barato = float("inf")
nome_mais_barato = ""

while True:
    nome_produto = str(input("Digite o nome do produto: "))
    preco_produto = float(input("Digite o preço do produto: "))
    continuar = str(input("Deseja continuar? S/N \n"))
    soma += preco_produto

    if continuar in "n":
        print("Programa encerrado!")
        break

    elif preco_produto < preco_mais_barato and preco_produto <= 1000:
        contagem += 1
        preco_mais_barato = preco_produto
        produto_mais_barato = nome_produto.lower().strip()

    else:
        while continuar in "1234567890abcdefghijklmopqrtuvxwyz!@#$%¨&*({[]};:\^~)": 
                print("Digite apenas S ou N!")
                continuar = str(input("Deseja continuar? S/N \n"))

print(f"""
Total: R${soma}
Quantidade de produtos que custaram menos de R$1.000: {contagem}
Nome do produto mais barato: {produto_mais_barato} 

""")



    



        


