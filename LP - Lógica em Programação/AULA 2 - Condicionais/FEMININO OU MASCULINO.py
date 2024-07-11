# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
# F - Feminino,
# M - Masculino,
# Outra letra qualquer - Sexo Inválido.

sexo = str(input("""
Informe a letra de acordo com o sexo:      
F - Feminino
M - Masculino
Outra letra - Sexo inválido
                 
Digite a letra: """)).upper()

if sexo == "F":
    print("Feminino.")

elif sexo == "M":
    print("Masculino.")

else:
    print("Sexo inválido.")
