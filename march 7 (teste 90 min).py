detalhes = []
conta = 0

tamanhos = {
    "pequena": 10,
    "media": 15,
    "grande": 20
}

ingredientes = {
    "Queijo",
    "Bacon",
    "Fiambre",
    "Ovo",
    "Cogumelos",
    "Azeitonas",
    "Ananas",
    "Atum",
    "Camarão",
    "Frango",
}

print("Bem vindo a Pizzeria Geometrica!")
tamanho = input("Que tamanho sera a sua pizza? (pequena, media ou grande): ")

if tamanho in tamanhos:
    detalhes.append(tamanho)
else: 
    print("Deve escolher 1 tamanho da lista.") 




print("Ingredientes:")
print("\n".join(ingredientes))
while conta < 5: 
    escolhaI = input("Escolha 5 ingredientes da lista: ")
    
    if escolhaI in ingredientes:
        detalhes.append(escolhaI)
        conta = conta + 1
    else:
        print("Escolha uma opção valida")


escolha = input("Pretende continuar com a preparação da pizza? (sim/nao) ")

if escolha == "sim":
    print("--Informação da entrada:", ", ".join(detalhes))



elif escolha == "nao":
    print("Pizza por cozer")

    
    
else:
    print("Escolha 'sim' ou 'nao'.")



class Pizza:
    def __init__(self, tamanho, ingredientes):
        self.base = "Tradicional"
        self.tamanho = tamanho
        self.ingredientes = ingredientes
        self.valor = tamanhos[tamanho]  

    def adicionar_ingrediente(self, ingrediente):
        if ingrediente in ingredientes and ingrediente not in self.ingredientes:
            self.ingredientes.append(ingrediente)

    def calcular_preco(self):
        return self.valor

    def atualizar_status(self, novo_status):
        self.status = novo_status

    def exibir_detalhes(self):
        return f"Tamanho: {self.tamanho} \n Ingredientes: {', '.join(self.ingredientes)}, Preço: {self.calcular_preco()}"

