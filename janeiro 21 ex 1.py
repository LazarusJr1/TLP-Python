saldo = 1000
choice = 0

while choice != 4:

    print("1: Consultar saldo")
    print("2: Depositar dinheiro")
    print("3: Retirar dinheiro")
    print("4: Sair ")
    choice = int(input("Choice: "))

    if choice == 1:
        print(f"--Saldo é {saldo}")
    
    elif choice == 2:
        depositar = int(input("--Quanto quer depositar?: "))
        if depositar > 0 and depositar != 0:
            saldo = depositar + saldo
        else:
            print("--INVALID NUMBER")
    
    elif choice == 3:
        retirar = int(input("--Quanto quer retirar?: "))
        if retirar > saldo or retirar == saldo or retirar < 0 or retirar == 0:
            print("--INVALID NUMBER")
        else:
            saldo = saldo - retirar
    else:
        print("--Se digitou 4, adeus. Se não, tente novamente.")