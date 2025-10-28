def celsius_para_fahrenheit(celsius):
    fahren = (celsius * 9/5) + 32
    return fahren

def main():
    try:
        celsius = float(input("digite a temperatura (em graus Celsius): "))
        fahren = celsius_para_fahrenheit(celsius)
        print(f"convertido para graus Fahrenheit é: {fahren:.2f}°F")
    except ValueError:
        print("NUMERO INVALIDO")


main()