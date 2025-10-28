class Tabuada:
    def __init__(self, numero, ate=10):
        self.numero = numero
        self.ate = ate
        self.resultados = {}  

    def __iter__(self):
        self.i = 1
        return self

    def __next__(self):
        if self.i <= self.ate:
            if self.i in self.resultados:
                resultado = self.resultados[self.i]
            else:
                resultado = self.numero * self.i
                self.resultados[self.i] = resultado
            texto = f"{self.numero} x {self.i} = {resultado}"
            self.i += 1
            return texto
        else:
            raise StopIteration



tabuada_7 = Tabuada(7)

print("Tabuada do 7:")
for linha in tabuada_7:
    print(linha)
