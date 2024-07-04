# Faça um programa que peça a idade, a altura, o cpf e o nome do usuário e imprima na tela a mensagem:
# Bem-vindo (usuário), seus dados foram cadastrados com sucesso. Idade = ‘’, altura = ‘’, cpf = ‘’.

idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
cpf = str(input("Digite o seu CPF: "))
nome = str(input("Digite seu nome: "))
print(f"Bem vindo, {nome}, seus dados foram cadastrados com sucesso. Idade = {idade}, altura = {altura}, cpf = {cpf}")