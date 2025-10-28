def contabilizar_numeros():
    contagem_positivos = 0
    contagem_negativos = 0

    while True:
        entrada = input("digite um numero ou 'sair': ")

        if entrada.lower() == 'sair':
            break

        try:
            n = float(entrada)

            if n >= 100:
                print("numero não pode ser mais que 100 burro")
                continue
            if n < 0:
                contagem_negativos += 1
            else:
                contagem_positivos += 1

        except ValueError:
            print("NUMERO não pode ser mais que 100 burro NUMERO é um NUMERO")

    print(f"numeros positivos menores que 100: {contagem_positivos}")
    print(f"numeros negativos menores que 100: {contagem_negativos}")
    print(f"numeros menor que 100 total: {contagem_negativos + contagem_positivos}")

contabilizar_numeros()