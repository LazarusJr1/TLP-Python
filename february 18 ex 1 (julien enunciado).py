# Enunciado:
# "criar um programa com menu visivel com as opções de adicionar tarefa, ver tarefas, remover tarefas e sair do programa."

carrinho = []
compra = "a"

while compra != "sair": # "if compra = sair exit the program"
    compra = input("------Opções\n-Adicionar tarefas (adicionar)\n-Listar tarefas (listar)\n-Remover tarefas (ex: remover tarefa1)\n-Sair (sair)\n------Escolha = ")
    
    if compra == "adicionar":
        adicionar = input("Que tarefa quer adicionar? (escreve o que quiser): ")
        carrinho.append(adicionar)
    
    elif compra == "listar":   ###################### LIST
        if not carrinho:  # checks if cart is empty
            print("Lista de tarefas esta vazio")
        else:
            print("--Tarefas na lista:", ", ".join(carrinho)) # carrinho list
   
    elif compra.startswith("remover "):  # works by checking if compra starts with "remover" in which case it removes whatever is in front of remover
        item_remover = compra.split("remover ")[1] 
        if item_remover in carrinho: # 21 and 22: check if indicated item exists
            carrinho.remove(item_remover) # removes said item if it does exist
            print("Item removida da lista")
        else:
            print("Item não esta na lista")
    
    elif compra == "sair": 
        if not carrinho: # checks if cart is empty
            print("Lista ta vazia mas ya ok tchau")
            break  # end
        else:
            print("Tchau!")
            break  # end
    
    else:
        print("Escolha não reconhecida. Tente novamente.")