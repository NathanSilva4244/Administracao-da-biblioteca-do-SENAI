import MovimentacaoDAO as db
def exibir_menu():
    print("\nMENU:")
    print("1. Listar movimentações")
    print("2. Atualizar movimentação")
    print("3. Buscar movimentação por ID")
    print("4. Cadastrar nova movimentação")
    print("5. Deletar movimentação por ID")
    print("6. Sair")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_mov()
        elif opcao == "2":
            atualizar_movimentacao()
        elif opcao == "3":
            buscar_movimentacao()
        elif opcao == "4":
            cadastrar_movimentacao()
        elif opcao == "5":
            deletar_movimentacao()
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")




def listar_mov():
    movimentacoes = db.listar_mov()
    print("Listando movimentações:")
    for mov in movimentacoes:
        print(mov)
def atualizar_movimentacao():
    id = input("Digite o ID da movimentação que deseja atualizar: ")
    quantidade = input("Nova quantidade: ")
    tipo = input("Novo tipo: ")
    data = input("Nova data (formato YYYY-MM-DD): ")
    material_didatico_id = input("Novo material didático ID: ")
    estoque_id = input("Novo estoque ID: ")
    db.atualizar_mov(id, quantidade, tipo, data, material_didatico_id, estoque_id)
    print("Movimentação atualizada com sucesso!")

def buscar_movimentacao():
    id = input("Digite o ID da movimentação que deseja buscar: ")
    movimentacao = db.buscar_mov(id)
    if movimentacao:
        print("Movimentação encontrada:")
        print(movimentacao)
    else:
        print("Movimentação não encontrada.")

def cadastrar_movimentacao():
    quantidade = input("Quantidade: ")
    tipo = input("Tipo: ")
    data = input("Data (formato YYYY-MM-DD): ")
    material_didatico_id = input("Material didático ID: ")
    estoque_id = input("Estoque ID: ")
    db.cadastrar_mov(quantidade, tipo, data, material_didatico_id, estoque_id)
    print("Movimentação cadastrada com sucesso!")

def deletar_movimentacao():
    id = input("Digite o ID da movimentação que deseja deletar: ")
    db.deletar_mov(id)
    print("Movimentação deletada com sucesso!")

if __name__ == "__main__":
    main()
