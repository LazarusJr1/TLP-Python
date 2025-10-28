def main():
    total = 0.0
    count = 0

    while True:
        try:
            numero = float(input("digite um numero real (ou 0 para terminar): "))

            if numero == 0:
                break

            total += numero
            count += 1
            print(f"Subtotal = {total:.6f}")

        except ValueError:
            print("NUMERO INVALIDO")

    if count > 0:
        media = total / count
        print(f"total = {total:.6f}")
        print(f"media = {media:.6f}")
    else:
        print("ERROR")

main()