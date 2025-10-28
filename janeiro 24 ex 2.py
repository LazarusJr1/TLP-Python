

produtos = {
    "camisa": 15,
    "calcas": 25,
    "casaco": 50,
    "t-shirt": 10
}

carrinho = []
compra = "a"

while compra != "sair": # "if compra = sair exit the program"
    compra = input("---Itens---\n1 - Camisa - 15€\n2 - Calças - 25€\n3 - Casaco - 50€\n4 - T-shirt - 10€\n---Opções---\nRemover - ex: remover calcas\nListar - listar\nSair - sair\nO que quer comprar? (escreva tudo em minusculas)    ")

    if compra in produtos: # checks if the value of compra is in "produtos" from line 3

        print(f"--Adicionou {compra} ao carrinho!!!") 
        carrinho.append(compra)  # adds procuct to cart
    
    elif compra == "listar":   ###################### LIST
        if not carrinho:  # checks if cart is empty
            print("Carrinho esta vazio")
        else:
            print("--Produtos no carrinho:", ", ".join(carrinho)) # carrinho list
            
            total = sum(produtos[item] for item in carrinho) # price list
            print(f"Total: {total}€")
   
    elif compra.startswith("remover "):  # works by checking if compra starts with "remover" in which case it removes whatever is in front of remover
        item_remover = compra.split("remover ")[1] 
        if item_remover in carrinho: # 31 and 32: check if indicated item exists
            carrinho.remove(item_remover) # removes said item if it does exist
            print("Item removido do carrinho")
        else:
            print("Item não esta no carrinho")
    
    elif compra == "sair": 
        if not carrinho: # checks if cart is empty
            print("Carrinho ta vazio mas ya ok tchau")
        else:
            total = sum(produtos[item] for item in carrinho)
            print("--Produtos comprados:", ", ".join(carrinho))
            print(f"--Total a pagar: {total}€")
            print("Tchau!")
            break  # end   
    
    else:
        print("Escolha não reconhecido. Tente novamente.")