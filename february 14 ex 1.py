alunos = []
menu = 100

def registar(nome, idade, nota1, nota2, nota3):
    class Aluno:
        def __init__(self, nome, idade, nota1, nota2, nota3):
            self.name = nome
            self.age = idade
            self.grade1 = nota1
            self.grade2 = nota2
            self.grade3 = nota3

    return Aluno(nome, idade, nota1, nota2, nota3)

def listar():       
    if alunos:  # checks for any registered aluno(s)
        print("Lista de Alunos:")
        for aluno in alunos:
            print(f"--- Nome: {aluno.name} \n-- Idade: {aluno.age} \n-- Notas: {aluno.grade1}, {aluno.grade2}, {aluno.grade3}")
    else:
        print("Nenhum aluno registado")

def calcular(nome):
    for aluno in alunos: # checks how many aluno in alunos (i think)
        if aluno.name == nome:
            media = (aluno.grade1 + aluno.grade2 + aluno.grade3) / 3
            if media > 7:
                print(f"A media de {aluno.name} é {media:.2f} e esta aprovado!")
            elif media < 7:
                print(f"A media de {aluno.name} é {media:.2f} e esta reprovado!")
            

            return
        else:
            print("Aluno não encontrado.")

while menu != 0:
    menu = input("--- 1 - Registar Alunos\n--- 2 - Listar Informação Alunos\n--- 3 - Exibir Notas e Media de Alunos\n--- 0 - Sair\nQual quer escolher?:   ")

    if menu == "1":
        nome = input("Insira o nome do aluno: ")
        idade = input("Insira a idade do aluno: ")
        nota1 = float(input("Insira a nota 1 do aluno: "))
        nota2 = float(input("Insira a nota 2 do aluno: "))
        nota3 = float(input("Insira a nota 3 do aluno: "))
        aluno = registar(nome, idade, nota1, nota2, nota3)
        ###################################################################
        alunos.append(aluno)
        if len(alunos) >= 5:
            print("Turma Completa")  
        else:
            print(f"Aluno registado: {aluno.name} \nIdade: {aluno.age} \nNotas: {aluno.grade1}, {aluno.grade2}, {aluno.grade3}")

    elif menu == "2":
        listar() 
        
    elif menu == "3":
        nome = input("Qual media quer calcular? (Insira nome de um aluno): ")
        calcular(nome)
        
    elif menu == "0":
        break

    else:
        print("ERROR: ESCOLHE UM DOS NUMEROS LISTADOS BURRO")