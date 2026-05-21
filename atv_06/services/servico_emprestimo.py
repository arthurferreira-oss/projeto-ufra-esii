from datetime import datetime

class ServicoEmprestimo:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def finalizar_devolucao(self, id_emprestimo):
        emprestimo = self.repositorio.buscar_por_id(id_emprestimo)
        if not emprestimo:
            return "Empréstimo não encontrado."

        data_atual = datetime.now()
        # Calcula a diferença de dias entre a data prevista e a entrega real
        atraso = (data_atual - emprestimo.data_devolucao_prevista).days

        # OCP em ação: O serviço não pergunta "quem você é?", 
        # ele apenas diz "calcule sua multa".
        multa = emprestimo.equipamento.calcular_multa(atraso)

        emprestimo.registrar_devolucao(data_atual, multa)
        self.repositorio.atualizar(emprestimo)
        
        return f"Devolução realizada. Multa: R$ {multa:.2f}"

    def listar_atrasados(self):
        atrasados = self.repositorio.buscar_atrasados()
        data_atual = datetime.now()
        
        resultado = []
        for emp in atrasados:
            atraso = (data_atual - emp.data_devolucao_prevista).days
            # Reutilização do método polimórfico elimina a duplicação de lógica.
            multa_estimada = emp.equipamento.calcular_multa(atraso)
            
            resultado.append({
                "equipamento": emp.equipamento.nome,
                "dias_atraso": atraso,
                "multa_atual": multa_estimada
            })
            
        return resultado