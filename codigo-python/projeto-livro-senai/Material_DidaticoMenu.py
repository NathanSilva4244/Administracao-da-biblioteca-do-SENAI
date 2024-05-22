import Material_DidaticoDAO as db

material_didatico = db.listar_material_didatico()

def exibir_menu():
    print("\nMENU:")
    print("1. Listar materiais didáticos")
    print("2. Buscar material didático por ID")
    print("3. Cadastrar novo material didático")
    print("4. Atualizar material didático")
    print("5. Deletar material didático por ID")
    print("6. Sair")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_material_didatico()
        elif opcao == "2":
            buscar_material_didatico_por_id()
        elif opcao == "3":
            cadastrar_material_didatico()
        elif opcao == "4":
            atualizar_material_didatico()
        elif opcao == "5":
            deletar_material_didatico()
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def listar_material_didatico():
    material_didatico = db.listar_material_didatico()
    print("Listando materiais didáticos:")
    for material in material_didatico:
        print(material)

def buscar_material_didatico_por_id():
    id = input("Digite o ID do material didático que deseja buscar: ")
    material_didatico = db.buscar_material_didatico_por_id(id)
    if material_didatico:
        print("Material didático encontrado:")
        print(material_didatico)
    else:
        print("Material didático não encontrado.")

def cadastrar_material_didatico():
    categoria = input("Categoria: ")
    titulo = input("Título: ")
    data_publicacao = input("Data de publicação (formato YYYY-MM-DD): ")
    db.cadastrar_material_didatico(categoria, titulo, data_publicacao)
    print("Material didático cadastrado com sucesso!")

def atualizar_material_didatico():
    id = input("Digite o ID do material didático que deseja atualizar: ")
    categoria = input("Nova categoria: ")
    titulo = input("Novo título: ")
    data_publicacao = input("Nova data de publicação (formato YYYY-MM-DD): ")
    db.atualizar_material_didatico(id, categoria, titulo, data_publicacao)
    print("Material didático atualizado com sucesso!")

def deletar_material_didatico():
    id = input("Digite o ID do material didático que deseja deletar: ")
    db.deletar_material_didatico(id)
    print("Material didático deletado com sucesso!")

if __name__ == "__main__":
    main()
