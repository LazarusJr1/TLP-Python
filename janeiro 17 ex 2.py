def verificar_numero():
    while True:
        try:
            n = int(input("digite um numero inteiro (1 a 10): "))

            if 0 <= n <= 10:
                print("O numero pertence ao intervalo")
                break
            else:
                print("não pertence ao intervalo. burro.")

        except ValueError:
            print("NUMERO INVALIDO")

    print("Fim do programa")

verificar_numero()