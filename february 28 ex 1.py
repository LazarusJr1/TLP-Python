# os comentários no codigo existem só para eu lembrar o que as coisas fazem quando for para apresentar daqui a ~1 semana

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False # se não estiver disponivel, exe linha 10
            print(f'O livro "{self.titulo}" foi emprestado com sucesso.') # <titulo> foi emprestado
        else:
            print(f'O livro "{self.titulo}" não está disponivel para empréstimo.')

    def devolver(self):
        self.disponivel = True # sets disponivel to true so it can be emprestado again
        print(f'O livro "{self.titulo}" foi devolvido com sucesso.')

    def informacoes(self):
        status = "Disponivel" if self.disponivel else "Indisponivel" # "if disponivel, write 'disponivel', else write 'indisponivel'"
        return f'Titulo: {self.titulo}, Autor: {self.autor}, Status: {status}'


class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro) # append adds the book to "self.livros[]" which is the list of books (if i SOMEHOW forget that)
        print(f'O livro "{livro.titulo}" foi adicionado à biblioteca.')

    def listar_livros(self):
        if not self.livros: # "if no books are in the library" but written in a quirky programming way
            print("Não há livros na biblioteca.")
            return
        for livro in self.livros: # "for every livro in self.livros (the list) print the livro info"
            print(livro.informacoes())

    def emprestar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo: # "if the user inputted a title that is the same as one of the titles in the list, empresta o livro"
                livro.emprestar()
                return
        print(f'O livro "{titulo}" não foi encontrado na biblioteca.')

    def devolver_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo: # "if the user inputted a title that is the same as one of the titles they have, devolver o livro"
                livro.devolver()
                return
        print(f'O livro "{titulo}" não foi encontrado na biblioteca.')


# Exemplo de uso do sistema
if __name__ == "__main__":
    biblioteca = Biblioteca()

    livro1 = Livro("1984", "George Orwell")
    livro2 = Livro("Blocks", "John Minecraft")
    livro3 = Livro("O Senhor dos Aneis", "Tolkien")


    print("Iniciando...\n")

    menu = input("Escolha uma opção\n 1- Listar livros\n 2- Emprestar livros\n 3- Devolver livros\n 4- Sair       ")

    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)
    biblioteca.adicionar_livro(livro3)

    d = 1
    while menu != 4:
        if menu == 1:
            print("\nLista de livros na biblioteca:")
            biblioteca.listar_livros()

        elif menu == 2:
            d = input("\nQual livro quer?")
            biblioteca.emprestar_livro(d)
            d = 1

        elif menu == 3:
            d = input("\nQual livro quer devolver?")
            biblioteca.devolver_livro(d)
            d = 1

            ###########################################################################################
            ###                                                                                     ###
            ### vou ser honesto stora, acho que este programa não funciona mas tive que entregar    ###
            ### para não ter zero, depois na aula vejamos                                           ###
            ###                                                                                     ###
            ###########################################################################################