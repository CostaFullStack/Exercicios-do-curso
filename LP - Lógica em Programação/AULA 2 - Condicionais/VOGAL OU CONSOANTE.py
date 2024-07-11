# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

vogal_consoante = str(input("Digite uma letra: ")).lower()

if vogal_consoante in "aáãàâeéèêiíìîoõôóòuúùû":
    print(f"A letra {vogal_consoante} é uma vogal.")

else:
    print(f"A letra {vogal_consoante} é uma consoante.")