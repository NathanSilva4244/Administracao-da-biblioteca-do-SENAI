import TurmaDAO as db


def exibir_menu():
    print("\nMENU:")
    print("1. Listar turma")
    print("2. Buscar turma por ID")
    print("3. Cadastrar novo turma")
    print("4. Atualizar turma")
    print("5. Deletar turma por ID")
    print("6. Sair")


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_turma()
        elif opcao == "2":
            buscar_turma()
        elif opcao == "3":
            cadastrar_turma_menu()
        elif opcao == "4":
            atualizar_turma_menu()
        elif opcao == "5":
            deletar_turma()
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


def listar_turma():
    turma = db.listar_turma()
    print("Listando turma :")
    for p in turma:
        print(p)


def buscar_turma():
    id = input("Digite o ID do turma que deseja buscar: ")
    turma = db.buscar_turma(id)
    if turma:
        print("turma encontrada:")
        print(turma)
    else:
        print("turma não encontrada.")


def cadastrar_turma_menu():
    def exibir_submenu():
        print("\nEscolha a categoria da turma:")
        print("1. Curso Livre")
        print("2. Graduação")
        print("3. Pós-Graduação")
        print("4. Curso Técnico")
        print("5. Aprendiz Senai")
        print("0. Voltar ao menu principal")

    while True:
        exibir_submenu()
        opcao = input("Digite o número correspondente à categoria da turma (ou 0 para voltar ao menu principal): ")

        if opcao == '0':
            print("Voltando ao menu principal...")
            break
        elif opcao in {'1', '2', '3', '4', '5'}:
            categoria = obter_categoria(int(opcao))
            nome = input("Digite o nome da turma: ")
            db.cadastrar_turma(categoria, nome)
            print("Turma cadastrada com sucesso!")
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


def atualizar_turma_menu():
    def exibir_submenu():
        print("\nEscolha a categoria da turma:")
        print("1. Curso Livre")
        print("2. Graduação")
        print("3. Pós-Graduação")
        print("4. Curso Técnico")
        print("5. Aprendiz Senai")
        print("0. Voltar ao menu principal")

    id = input("Digite o ID do turma que deseja atualizar: ")
    nome = input("Novo nome da turma: ")

    while True:
        exibir_submenu()
        opcao = input("Digite o número correspondente à categoria da turma (ou 0 para voltar ao menu principal): ")

        if opcao == '0':
            print("Voltando ao menu principal...")
            break
        elif opcao in {'1', '2', '3', '4', '5'}:
            categoria = obter_categoria(int(opcao))
            db.atualizar_turma(id, categoria, nome)
            print("turma atualizada com sucesso!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


def obter_categoria(opcao):
    categorias = {
        1: 'Curso Livre',
        2: 'Graduação',
        3: 'Pós Graduação',
        4: 'Curso Técnico',
        5: 'Aprendiz Senai'
    }
    return categorias[opcao]


def deletar_turma():
    id = input("Digite o ID do turma que deseja deletar: ")
    db.deletar_turma(id)
    print("turma deletado com sucesso!")


if __name__ == "__main__":
    main()
