import ArmarioDAO as db

def exibir_menu():
    print("\nMENU:")
    print("1. Listar armário")
    print("2. Buscar armário por ID")
    print("3. Cadastrar novo armário")
    print("4. Atualizar armário")
    print("5. Deletar armário por ID")
    print("6. Sair")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_armario()
        elif opcao == "2":
            buscar_armario()
        elif opcao == "3":
            cadastrar_armario()
        elif opcao == "4":
            atualizar_armario()
        elif opcao == "5":
            deletar_armario()
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def listar_armario():
    armario = db.listar_armario()
    print("Listando armário:")
    for a in armario:
        print(a)

def buscar_armario():
    id = input("Digite o ID do armário que deseja buscar: ")
    armario = db.buscar_armario(id)
    if armario:
        print("Armário encontrado:")
        print(armario)
    else:
        print("Armário não encontrado.")

def cadastrar_armario():
    nome = input("nome: ")
    db.cadastrar_armario(nome)
    print("Armário cadastrado com sucesso!")

def atualizar_armario():
    id = input("Digite o ID do armário que deseja atualizar: ")
    nome = input("Novo armário: ")
    db.atualizar_armario(id, nome)
    print("Armário atualizado com sucesso!")

def deletar_armario():
    id = input("Digite o ID do armário que deseja deletar: ")
    db.deletar_armario(id)
    print("Armário deletado com sucesso!")

if __name__ == "__main__":
    main()
