# Crie uma função chamada concatenar_strings que aceita um número variável de strings como argumentos posicionais (usando *args). A função deve concatenar todas as strings em uma única string e retorná-la.

def concatenar_strings(*args):
    contador = ""
    for i in args:
        contador += i    
    return contador

resultado = concatenar_strings("Lilya", " ", "4-ever")

print(f"Strings em uma única:\n{resultado}")