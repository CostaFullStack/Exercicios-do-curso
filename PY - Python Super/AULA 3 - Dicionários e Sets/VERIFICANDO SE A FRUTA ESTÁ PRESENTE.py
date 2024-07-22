# Verifique se a fruta "banana" está presente no conjunto frutas e imprima o resultado.

frutas = set()

frutas.update(["maçã", "banana", "uva", "laranja", "morango"])

print("banana".lower() in frutas)