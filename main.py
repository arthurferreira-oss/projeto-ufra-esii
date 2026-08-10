from app.sistema import SistemaDeEmprestimos


def main():
    sistema = SistemaDeEmprestimos()  # A fachada monta tudo em uma linha

    while True:
        print("\n1-Registrar 2-Devolver 3-Atrasados 0-Sair")
        opcao = input("Opção: ")

        if opcao == "1":
            try:
                equipamento_id = int(input("ID equipamento: "))
                nome = input("Nome: ")
                email = input("Email: ")
                dias = int(input("Dias: "))
                sistema.registrar(equipamento_id, nome, email, dias)
            except ValueError:
                print("Por favor, insira valores numéricos válidos para ID e Dias.")

        elif opcao == "2":
            try:
                emprestimo_id = int(input("ID empréstimo: "))
                sistema.devolver(emprestimo_id)
            except ValueError:
                print("Por favor, insira um ID numérico válido.")

        elif opcao == "3":
            sistema.listar_atrasados()

        elif opcao == "0":
            break


if __name__ == "__main__":
    main()
