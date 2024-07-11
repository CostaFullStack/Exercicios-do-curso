# Neste módulo você construirá um simulador de cadastro de senha e inicialização de celular. 

# Parte 1) Vamos supor que o usuário acabou de comprar um celular na loja e após a primeira carga, ele liga o celular pela primeira vez. Ao iniciar o celular, a primeira coisa que aparece na tela é o pedido para cadastrar a senha e, logo após, confirmar a senha. Essa é a sua primeira tarefa. Construa o pedido de senha e confirmação. Se a senha confirmada estiver correta, exiba a mensagem: Senha correta. Bem-vindo. Senão, exiba a mensagem: Senha incorreta. Tente novamente.
print("O celular está sendo iniciado...")

senha = str(input("Insira a senha: "))
confirma_senha = str(input("Confirme a sua senha: "))

if senha == confirma_senha:
    print("Senha correta. Bem vindo.")
else:
    print("Senha incorreta. Tente novamente.")


# Parte 2) se o aprendizado desta aula para implementar o while ao projeto. A senha cadastrada anteriormente precisa de um looping, caso o usuário digite a senha errada. A primeira senha deve ser igual a confirmação de senha. Enquanto o usuário não confirmar, o seu programa exibirá a mensagem: “Senha incorreta, tente novamente.”
print("O celular está sendo iniciado...")

senha = str(input("Insira a senha: "))

while True:
    confirma_senha = str(input("Confirme a sua senha: "))
    if senha == confirma_senha:
        print("Senha correta. Bem vindo.")
        break
    else:
        print("Senha incorreta. Tente novamente.")

# Parte 3) Use o aprendizado desta aula para implementar o for ao projeto. Após implementar o sistema de cadastro de senha, chegou a hora de entrar no sistema operacional. Após ligar o celular, é necessário inserir a senha cadastrada. São 3 tentativas até o telefone bloquear. Se o usuário acertar a senha, escreva a mensagem: “bem vindo.” Se o usuário errar a senha, escreva a mensagem: “Senha incorreta. Você tem x tentativas até o bloqueio.

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







