order = []
menu = "a"
tamanho = "a"
temp = "a"

while menu != "sair": # "if menu = sair exit the program"
    menu = input("Qual entrada deseja preparar?\n-Pão de alho\n-Bruschetta\n-Queijo frito\nEscolha: ")

    if menu == "pão de alho" or menu == "bruschetta" or menu == "queijo frito":
          order.append(menu)

          
          tamanho = input("Qual tamanho de entrada quer? (individual, medio ou familiar): ")
          while tamanho != "individual" or tamanho != "medio" or tamanho != "familiar":
            
            if tamanho == "individual" or menu == "medio" or menu == "familiar":
                order.append(tamanho)

                temp = input("Tamanho escolhido! Deseja a sua entrada 'bem quente'? (sim/nao): ")
            if temp == "sim":
                order.append(temp)
                print("A aquecer...")
                print("--Informação da entrada:", ", ".join(order))
            elif temp == "nao":
                order.append(temp)
                print("ok")
                print("--Informação da entrada:", ", ".join(order))

          else:
            print("Deve escolher 1 tamanho da lista.")    
    else:
        print("Deve escolher 1 entrada da lista.")
   