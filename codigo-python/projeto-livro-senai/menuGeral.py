import ArmarioMenu
import EstoqueMenu
import Material_DidaticoMenu
import MovimentacaoMenu
import ObservacaoMenu
import ProfessorMenu
import RepografiaMenu
import TurmaMenu

while True:
    print("\nMENU:")
    print("1. MOVIMENTAÇÃO")
    print("2. MATERIAL DIDATICO")
    print("3. ESTOQUE")
    print("4. PROFESSOR ")
    print("5. TURMA ")
    print("6. ARMARIO ")
    print("7. OBSERVAÇÃO ")
    print("8. REPOGRAFIA ")
    print("9. SAIR")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        MovimentacaoMenu.main()
    elif opcao == "2":
        Material_DidaticoMenu.main()
    elif opcao == "3":
        EstoqueMenu.main()
    elif opcao == "4":
        ProfessorMenu.main()
    elif opcao == "5":
        TurmaMenu.main()
    elif opcao == "6":
        ArmarioMenu.main()
    elif opcao == "7":
        ObservacaoMenu.main()
    elif opcao == "8":
        RepografiaMenu.main()
    elif opcao == "9":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
