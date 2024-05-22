import ProfessorDAO as db

def exibir_menu():
    print("\nMENU:")
    print("1. Listar professor")
    print("2. Buscar professor por ID")
    print("3. Cadastrar novo professor")
    print("4. Atualizar professor")
    print("5. Deletar professor por ID")
    print("6. Sair")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_professor()
        elif opcao == "2":
            buscar_professor()
        elif opcao == "3":
            cadastrar_professor()
        elif opcao == "4":
            atualizar_professor()
        elif opcao == "5":
            deletar_professor()
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def listar_professor():
    professor = db.listar_professor()
    print("Listando professor :")
    for p in professor:
        print(p)

def buscar_professor():
    id = input("Digite o ID do professor que deseja buscar: ")
    professor = db.buscar_professor(id)
    if professor:
        print("professor encontrado:")
        print(professor)
    else:
        print("professor não encontrado.")

def cadastrar_professor():
    nome = input("Nome: ")
    db.cadastrar_professor(nome)
    print("professor cadastrado com sucesso!")

def atualizar_professor():
    id = input("Digite o ID do professor que deseja atualizar: ")
    nome = input("Novo professor: ")
    db.atualizar_professor(id, nome)
    print(" professor atualizado com sucesso!")

def deletar_professor():
    id = input("Digite o ID do professor que deseja deletar: ")
    db.deletar_professor(id)
    print("professor deletado com sucesso!")

if __name__ == "__main__":
    main()
