class Jogador:
    def __init__(self, nome):
        self.nome = nome  # Nome do jogador
        self.nivel = 0    # Nível inicial
        self.experiencia = 0  # Experiência inicial

    def ganhar_xp(self, valor):
        self.experiencia += valor  # aumenta a experiência do jogador baseado em oq o utilizador 

        while self.experiencia >= 100:# "enquanto self.experiencia maior ou igual a 100"
            self.experiencia = self.experiencia - 100 # could use -= and += to be more efficient on 11 and 12 but i'm stubborn
            self.nivel = self.nivel + 1  

    def exibir_status(self):
        print(f"Nome: {self.nome}, Nível: {self.nivel}, Experiência: {self.experiencia}")

# 1
jogador = Jogador(input("Insira o seu nome: "))

# 2 - exibir status inicial
jogador.exibir_status()

# 3 - dar 50 pontos
jogador.ganhar_xp(50)
jogador.exibir_status()

# 4 - dar mais 60 pontos
jogador.ganhar_xp(60)
jogador.exibir_status()

# 5 - mostrar print final
print(f"{jogador.nome} tem {jogador.experiencia} pontos de experiência e está no nível {jogador.nivel}.")