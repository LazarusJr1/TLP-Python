q = int(input("Quantos numeros vai digitar?: "))

soma = 0 

for i in range(q):
    numero = int(input("Digite um numero: "))
    soma += numero  

print("Soma dos numeros digitados: ", soma)