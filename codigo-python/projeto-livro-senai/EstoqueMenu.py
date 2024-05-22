import EstoqueDAO as db

def exibir_menu():
    print("\nMENU:")
    print("1. Listar estoque")
    print("2. Buscar estoque por ID")
    print("3. Cadastrar novo estoque")
    print("4. Atualizar estoque")
    print("5. Deletar estoque por ID")
    print("6. Sair")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_estoque()
        elif opcao == "2":
            buscar_estoque()
        elif opcao == "3":
            cadastrar_estoque()
        elif opcao == "4":
            atualizar_estoque()
        elif opcao == "5":
            deletar_estoque()
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def listar_estoque():
    estoque = db.listar_estoque()
    print("Listando estoque:")
    for material in estoque:
        print(material)

def buscar_estoque():
    id = input("Digite o ID do estoque que deseja buscar: ")
    estoque = db.buscar_estoque(id)
    if estoque:
        print("estoque encontrado:")
        print(estoque)
    else:
        print("estoque não encontrado.")

def cadastrar_estoque():
    categoria = input("Categoria: ")
    titulo = input("Título: ")
    data_publicacao = input("Data de publicação (formato YYYY-MM-DD): ")
    db.cadastrar_estoque(categoria, titulo, data_publicacao)
    print("estoque cadastrado com sucesso!")

def atualizar_estoque():
    id = input("Digite o ID do estoque que deseja atualizar: ")
    descricao = input("Descrição: ")
    numero_nota = input("Número de nota: ")
    material_didatico_id = input("ID do material didático: ")
    db.atualizar_estoque(id, descricao, numero_nota, material_didatico_id)
    print("Estoque atualizado com sucesso!")

def deletar_estoque():
    id = input("Digite o ID do estoque que deseja deletar: ")
    db.deletar_estoque(id)
    print("estoque deletado com sucesso!")

if __name__ == "__main__":
    main()
