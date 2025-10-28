class Veiculo:
    def __init__(self, modelo, marca, ano, consumo):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.consumo = consumo
        self.deposito_combustivel = 0.0

    def abastecer(self, litros):
        self.deposito_combustivel += litros
        print(f"Abastecido {litros} litros. Nível atual: {self.deposito_combustivel:.2f} litros.")

    def conduzir(self, distancia):
        consumo_necessario = distancia / self.consumo
        if consumo_necessario > self.deposito_combustivel:
            print("Combustível insuficiente para a viagem.")
        else:
            self.deposito_combustivel -= consumo_necessario
            print(f"Conduzido {distancia} km. Combustível restante: {self.deposito_combustivel:.2f} litros.")

    def exibir_informacoes(self):
        print(f"Modelo: {self.modelo}, Marca: {self.marca}, Ano: {self.ano}, Consumo: {self.consumo} km/l, Combustível: {self.deposito_combustivel:.2f} litros.")


class Frota:
    def __init__(self):
        self.veiculos = []

    def adicionar_veiculo(self, veiculo):
        self.veiculos.append(veiculo)
        print(f"Veículo {veiculo.modelo} adicionado à frota.")

    def listar_veiculos(self):
        if not self.veiculos:
            print("Nenhum veículo registrado.")
            return
        for veiculo in self.veiculos:
            veiculo.exibir_informacoes()

    def encontrar_veiculo(self, modelo):
        for veiculo in self.veiculos:
            if veiculo.modelo == modelo:
                return veiculo
        print("Veículo não encontrado.")
        return None


def menu():
    frota = Frota()
    while True:
        print("\nMenu:")
        print("1. Adicionar veículo")
        print("2. Listar veículos")
        print("3. Encontrar veículo")
        print("4. Abastecer veículo")
        print("5. Conduzir veículo")
        print("6. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            modelo = input("Modelo: ")
            marca = input("Marca: ")
            ano = int(input("Ano: "))
            consumo = float(input("Consumo (km/l): "))
            veiculo = Veiculo(modelo, marca, ano, consumo)
            frota.adicionar_veiculo(veiculo)
        
        elif opcao == '2':
            frota.listar_veiculos()
        
        elif opcao == '3':
            modelo = input("Digite o modelo do veículo que deseja encontrar: ")
            veiculo = frota.encontrar_veiculo(modelo)
            if veiculo:
                veiculo.exibir_informacoes()
        
        elif opcao == '4':
            modelo = input("Digite o modelo do veículo que deseja abastecer: ")
            veiculo = frota.encontrar_veiculo(modelo)
            if veiculo:
                litros = float(input("Quantos litros deseja abastecer? "))
                veiculo.abastecer(litros)
        
        elif opcao == '5':
            modelo = input("Digite o modelo do veículo que deseja conduzir: ")
            veiculo = frota.encontrar_veiculo(modelo)
            if veiculo:
                distancia = float(input("Qual a distância a ser percorrida (em km)? "))
                veiculo.conduzir(distancia)
        
        elif opcao == '6':
            print("Saiu do sistema...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()