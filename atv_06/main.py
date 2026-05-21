from services.servico_emprestimo import ServicoEmprestimo

# 1. Como não há uma classe dentro de repositorio_emprestimo.py,
# criamos um repositório simulado em memória para o serviço poder rodar
class RepositorioEmMemoria:
    def __init__(self):
        self.emprestimos = {}

    def buscar_por_id(self, id_emprestimo):
        return self.emprestimos.get(id_emprestimo)

    def atualizar(self, emprestimo):
        self.emprestimos[emprestimo.id] = emprestimo

    def buscar_atrasados(self):
        # Retorna uma lista vazia só para não quebrar a listagem
        return []

def menu():
    # 2. Instanciamos o repositório simulado
    repositorio_real = RepositorioEmMemoria()
    
    # 3. Injetamos o repositório no construtor do ServicoEmprestimo (DIP Aplicado!)
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