# Faça um programa em python que determine em duas variáveis (senha e email) e que contenha uma senha e um email cadastrados antecipadamente, em seguida solicite ao usuário uma senha e um email e utilize o laço de repetição juntamente com a estrutura de condição para verificar se o email e a senha digitado pelo usuário é igual ao email e senha cadastrados antecipadamente. E enquanto a senha e o email que o usuário digitou não for igual ao email e senha cadastrados ele continue em um loop.

senha = "Lilya4-ever"
email = "prova@example.com.br"

while True:
    senha_confirma = str(input("Confirme a senha cadastrada: "))
    email_confirma = str(input("Confirme o email cadastrado: "))
    if senha_confirma != senha or email_confirma != email:
        print("Erro! Senha ou email incorretos!")
        
    else:
        print("Senha e e-mail corretos.")
