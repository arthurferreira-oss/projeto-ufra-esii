from services.servico_emprestimo import ServicoEmprestimo

class RepositorioEmMemoria:
    def __init__(self):
        self.emprestimos = {}

    def buscar_por_id(self, id_emprestimo):
        return self.emprestimos.get(id_emprestimo)

    def atualizar(self, emprestimo):
        self.emprestimos[emprestimo.id] = emprestimo

    def buscar_atrasados(self):
        return []

def menu():

    repositorio_real = RepositorioEmMemoria()
    
    servico = ServicoEmprestimo(repositorio_real)
    
    while True:
        print("\n--- SISTEMA DE EMPRÉSTIMOS UFRA ---")
        print("1. Finalizar Devolução")
        print("2. Listar Atrasados")
        print("3. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            try:
                id_emp = int(input("ID do Empréstimo para devolução: "))
                mensagem = servico.finalizar_devolucao(id_emp)
                print(mensagem)
            except ValueError:
                print("Por favor, digite um ID válido (número).")
                
        elif opcao == "2":
            atrasados = servico.listar_atrasados()
            if not atrasados:
                print("Nenhum equipamento atrasado no momento.")
            for item in atrasados:
                print(f"Equipamento: {item['equipamento']} | Dias: {item['dias_atraso']} | Multa: R$ {item['multa_atual']:.2f}")
                
        elif opcao == "3":
            print("Saindo do sistema...")
            break

if __name__ == "__main__":
    menu()