# Faça um programa utilizando o comando while que mostra uma contagem regressiva na tela, iniciando em 10 e terminando em 0. Mostrar uma mensagem “FIM! ”após a contagem.

# com for
for i in range(10,-1,-1):
    print(i)
print("FIM!")

# com while
contagem = 10

while contagem > 0:
    print(contagem)
    contagem -= 1

print("FIM!")
