# # Atividade Prática) 
# 1. Faça um Programa que mostre a mensagem "olá mundo" na tela.
# 2. Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
# 3. Faça um programa que peça a idade, a altura, o cpf e o nome do usuário e imprima na tela a mensagem:
# Bem-vindo (usuário), seus dados foram cadastrados com sucesso. Idade = ‘’, altura = ‘’, cpf = ‘’.

# 1.
print("Olá mundo.")

# 2.
numero = float(input("Digite um número: "))
print(f"O número informado foi: {numero}")

# 3.
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
cpf = str(input("Digite o seu CPF: "))
nome = str(input("Digite seu nome: "))
print(f"Bem vindo, {nome}, seus dados foram cadastrados com sucesso. Idade = {idade}, altura = {altura}, cpf = {cpf}")