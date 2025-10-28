filmes = []
choice = 0

def adicionar_filme():
    titulo = input("Film Title: ")
    ano = input("Film Release Year: ")
    genero = input("Film Genre: ")
    filmes.append({"titulo": titulo, "ano": ano, "genero": genero})
    print("--Film added successfully.")

def listar_filmes():
    if not filmes:
        print("--No film registered.")
    else:
        for filme in filmes:
            print(f"Title: {filme['titulo']}, Year: {filme['ano']}, Genre: {filme['genero']}")

def filtrar_por_genero():
    genero = input("Genre to filter by: ")
    encontrados = [f for f in filmes if f['genero'].lower() == genero.lower()]
    if encontrados:
        for filme in encontrados:
            print(f"Title: {filme['titulo']}, Year: {filme['ano']}")
    else:
        print("--No film found in that genre.")

def procurar_por_nome():
    nome = input("Film Name: ")
    encontrados = [f for f in filmes if nome.lower() in f['titulo'].lower()]
    if encontrados:
        for filme in encontrados:
            print(f"Title: {filme['titulo']}, Year: {filme['ano']}, Genre: {filme['genero']}")
    else:
        print("--Film not found.")
############################################################################################
while choice != 5:
    print("\n1: Add new film")
    print("2: List all films")
    print("3: Filter by genre")
    print("4: Search by name")
    print("5: Exit")
    try:
        choice = int(input("Choice: "))
    except ValueError:
        print("--INVALID, PICK A NUMBER 1 - 5.")
        continue

    if choice == 1:
        adicionar_filme()
    elif choice == 2:
        listar_filmes()
    elif choice == 3:
        filtrar_por_genero()
    elif choice == 4:
        procurar_por_nome()
    elif choice == 5:
        print("--Exiting program...")
    else:
        print("--Escolha um número de 1 a 5, por favor.")

