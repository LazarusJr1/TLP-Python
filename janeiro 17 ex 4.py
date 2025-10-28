def converter_segundos(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = segundos % 60
    return horas, minutos, segundos_restantes

def main():
    try:
        segundos = int(input("digite um valor em segundos: "))
        
        if segundos < 0:
            print("tem que ser numero inteiro não negativo")
            return
        
        horas, minutos, segundos_restantes = converter_segundos(segundos)
        
        print(f"{segundos} segundos equivalem a {horas} horas, {minutos} minutos e {segundos_restantes} segundos.")
    except ValueError:
        print("NUMERO INVALIDO")

main()