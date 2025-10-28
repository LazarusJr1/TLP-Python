age = int(input("Idade: "))

if age < 12:
    print ("A sessão de cinema só é permitida a maiores de 12 anos")
else:
    print("P - Plateia")
    print("B - 1 Balcão")
    print("S - Balcão Superior")

    zona = str(input())

    if zona.upper() == "P":
        print("Preço a pagar: 12")
    elif zona.upper() == "B":
        print("Preço a pagar: 15")
    elif zona.upper() == "S":
        print("Preço a pagar: 10.50")
    else:
        print("Zona introduzida invalida")