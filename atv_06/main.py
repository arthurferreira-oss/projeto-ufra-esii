from services.servico_emprestimo import ServicoEmprestimo

def menu():
    servico = ServicoEmprestimo()
    
    while True:
        print("\n--- SISTEMA DE EMPRÉSTIMOS UFRA ---")
        print("1. Registrar Empréstimo")
        print("2. Devolver Equipamento")
        print("3. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            id_eq = int(input("ID do Equipamento: "))
            nome = input("Seu nome: ")
            email = input("Seu e-mail: ")
            dias = int(input("Quantidade de dias: "))
            
            sucesso = servico.registrar(id_eq, nome, email, dias)
            if sucesso:
                print("Empréstimo realizado com sucesso!")
            else:
                print("Erro: Equipamento indisponível ou não encontrado.")
                
        elif opcao == "3":
            break

if __name__ == "__main__":
    menu()