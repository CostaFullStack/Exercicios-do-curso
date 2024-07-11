# Após ligar o celular, o usuário é solicitado a inserir a senha cadastrada.
# 1. São permitidas 3 tentativas até que o telefone seja bloqueado.
# 2. Se o usuário acertar a senha, uma mensagem de boas-vindas é exibida: "Bem-vindo."
# 3. Se o usuário errar a senha, uma mensagem informando o erro é exibida, junto com o número de tentativas restantes até o bloqueio do telefone.

tentativas = 3
senha = "Lilya4-ever"

print(f"Você possui {tentativas} tentativas até o bloqueio!")

for i in range (tentativas,-1,-1):
    confirma_senha = str(input("Insira a senha cadastrada: "))
    tentativas -= 1
    if tentativas == 0:
        print("Acesso bloqueado!")
        break
    elif confirma_senha != senha:
        print(f"Senha incorreta. Você possui {tentativas} tentativas até o bloqueio.")
    else:
        print("Acesso bloqueado!")
        break
