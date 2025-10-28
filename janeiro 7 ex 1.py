numeros = []

for i in range(15):
    numero = float(input(f"Digite o {i + 1} número: "))
    numeros.append(numero)  # adds number to the list


contagem = len(numeros) / 2.5  # honestamente não faço a minima ideia de como isto funciona mas acho que faz o que é suposto fazer ???

print(f"Numeros contados a cada 2,5: {contagem}")

soma = 0 
media = 0

for i in range(len(numeros)):
    soma = soma + numeros[i]

    media = soma / 15
print(f"Media: {media}")