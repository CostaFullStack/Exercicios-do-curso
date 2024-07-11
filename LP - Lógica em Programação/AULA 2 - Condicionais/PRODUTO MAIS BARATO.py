# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

primeiro_produto = float(input(f"Digite o preço do primeiro produto: "))
segundo_produto = float(input(f"Digite o preço do segundo produto: "))
terceiro_produto = float(input(f"Digite o preço do terceiro produto: "))

if primeiro_produto < segundo_produto and primeiro_produto < terceiro_produto:
    print(f"O produto mais barato a ser comprado é o primeiro produto. Valor: R${primeiro_produto}")

elif segundo_produto < primeiro_produto and segundo_produto < terceiro_produto:
    print(f"O produto mais barato a ser comprado é o segundo produto. Valor: R${segundo_produto}")

else:
    print(f"O produto mais barato a ser comprado é o segundo produto. Valor: R${terceiro_produto}")