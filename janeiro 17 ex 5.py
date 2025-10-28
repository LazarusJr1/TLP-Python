def contar_numeros():
    contagem_maiores = 0
    contagem_menores = 0

    for i in range(10):
        try:
            n = float(input(f"Digite o {i + 1}º número: "))

            if n > 25:
                contagem_maiores += 1
            elif n < 25:
                contagem_menores += 1

        except ValueError:
            print("NUMERO INVALIDO")
            return 

    print(f"maiores que 25: {contagem_maiores}")
    print(f"menores que 25: {contagem_menores}")

contar_numeros()