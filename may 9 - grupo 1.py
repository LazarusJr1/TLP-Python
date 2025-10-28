# define a classe Pessoa com nome e idade
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome  # Atributo para guardar o nome
        self.idade = idade  # Atributo para guardar a idade

class Registo:
    def __init__(self):
        self.lista = [] 
        self.i = 0     

    def adicionar(self, pessoa):
        def maior_idade(self):
            return self.idade >= 18
        pessoa.e_maior = maior_idade.__get__(pessoa)  

        def saudacao(self):
            return f"Ola, eu sou {self.nome} e tenho {self.idade} anos."
        pessoa.saudacao = saudacao.__get__(pessoa)  

        self.lista.append(pessoa)  

    def __iter__(self):
        self.i = 0  
        return self

    def __next__(self):
        if self.i < len(self.lista):
            p = self.lista[self.i]  
            self.i += 1             
            return p
        else:
            raise StopIteration  

# --- programa começa ---
registo = Registo() 

print("--- Registo de Pessoas ---")

while True:
    nome = input("Introduz um nome (ou 'sair'): ") 
    if nome == "sair":  
        break
    idade = input("Idade: ")  
    if not idade.isdigit():   
        print("Idade invalida.")  
        continue  
    p = Pessoa(nome, int(idade))  
    registo.adicionar(p) 

print("\n--- Lista de Pessoas ---")
for p in registo: 
    print(p.saudacao())
    print("Maior de idade:", "Sim" if p.e_maior() else "Não")  
