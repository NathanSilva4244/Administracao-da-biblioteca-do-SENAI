import ObservacaoDAO as db
def exibir_menu():
    print("\nMENU:")
    print("1. Listar observacao")
    print("2. Atualizar observacao")
    print("3. Buscar observacao por ID")
    print("4. Fazer nova observacao")
    print("5. Deletar observacao por ID")
    print("6. Sair")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_obs()
        elif opcao == "2":
            atualizar_observacao()
        elif opcao == "3":
            buscar_observacao()
        elif opcao == "4":
            cadastrar_observacao()
        elif opcao == "5":
            deletar_observacao()
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")




def listar_obs():
    observacao = db.listar_observacao()
    print("Listando observacao:")
    for obs in observacao:
        print(obs)
def atualizar_observacao():
    id = input("Digite o ID da observacao que deseja atualizar: ")
    data_observacao = input("Nova data (formato YYYY-MM-DD): ")
    professor_id = input("Iforme o ID do Professor: ")
    descricao = input("Descrição: ")
    db.atualizar_obs(id, data_observacao, professor_id, descricao)
    print("observacao atualizada com sucesso!")

def buscar_observacao():
    id = input("Digite o ID da observacao que deseja buscar: ")
    observacao = db.buscar_obs(id)
    if observacao:
        print("observacao encontrada:")
        print(observacao)
    else:
        print("observacao não encontrada.")

def cadastrar_observacao():
    data_observacao = input("Data (formato YYYY-MM-DD): ")
    professor_id = input("ID Professor: ")
    descricao = input("descricao: ")
    db.cadastrar_obs(data_observacao, professor_id, descricao)
    print("observacao cadastrada com sucesso!")

def deletar_observacao():
    id = input("Digite o ID da observacao que deseja deletar: ")
    db.deletar_observacao(id)
    print("observacao deletada com sucesso!")

if __name__ == "__main__":
    main()
