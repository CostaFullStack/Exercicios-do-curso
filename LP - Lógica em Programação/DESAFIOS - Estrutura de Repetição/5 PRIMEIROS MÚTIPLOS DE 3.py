# Faça um programa que determine o mostre os cinco primeiros múltiplos de 3, considerando números maiores que 0.

# com for
print(f"Os primeiros múltiplos de 3, considerando números maiores que 0 são:")

for i in range(1,16):
    if i % 3 == 0:
        print(i)

# com while
multiplo = 0

print(f"Os primeiros múltiplos de 3, considerando números maiores que 0 são:")

while multiplo < 15:
        multiplo += 3
        print(multiplo)


