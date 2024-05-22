import RepografiaDAO as db

def exibir_menu():
    print("\nMENU:")
    print("1. Listar repografias")
    print("2. Buscar repografia por ID")
    print("3. Cadastrar nova repografia")
    print("4. Atualizar repografia")
    print("5. Deletar repografia por ID")
    print("6. Sair")

def listar_repografias():
    repografias = db.listar_repografia()
    print("Listando repografias:")
    for repografia in repografias:
        print(repografia)

def buscar_repografia():
    id = input("Digite o ID da repografia que deseja buscar: ")
    repografia = db.buscar_repografia(id)
    if repografia:
        print("Repografia encontrada:")
        print(repografia)
    else:
        print("Repografia não encontrada.")

def cadastrar_repografia():
    data = input("Data: ")
    quantidade = input("Quantidade: ")
    material_didatico_id = input("ID do material didático: ")
    professor_id = input("ID do professor: ")
    db.cadastrar_repografia(data, quantidade, material_didatico_id, professor_id)
    print("Repografia cadastrada com sucesso!")

def atualizar_repografia():
    id = input("Digite o ID da repografia que deseja atualizar: ")
    data = input("Nova data: ")
    quantidade = input("Nova quantidade: ")
    material_didatico_id = input("Novo ID do material didático: ")
    professor_id = input("Novo ID do professor: ")
    db.atualizar_repografia(id, data, quantidade, material_didatico_id, professor_id)
    print("Repografia atualizada com sucesso!")

def deletar_repografia():
    id = input("Digite o ID da repografia que deseja deletar: ")
    db.deletar_repografia(id)
    print("Repografia deletada com sucesso!")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_repografias()
        elif opcao == "2":
            buscar_repografia()
        elif opcao == "3":
            cadastrar_repografia()
        elif opcao == "4":
            atualizar_repografia()
        elif opcao == "5":
            deletar_repografia()
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
