# Responsabilidade: Coordenar as regras de negócio de empréstimos.
from repositories.repositorio_emprestimo import RepositorioEmprestimo
from services.notificador import Notificador
from models.emprestimo import Emprestimo
from datetime import date, timedelta

class ServicoEmprestimo:
    def __init__(self):
        # Conforme item 2.3 do roteiro, criamos as dependências aqui por enquanto
        self.repo = RepositorioEmprestimo()
        self.notificador = Notificador()

    def registrar(self, equip_id: int, nome: str, email: str, dias: int) -> bool:
        equip = self.repo.buscar_equipamento(equip_id)
        if equip and equip.disponivel:
            novo_emprestimo = Emprestimo(
                id=len(self.repo.emprestimos) + 1,
                equip_id=equip_id,
                nome_usuario=nome,
                email_usuario=email,
                data_emprestimo=date.today(),
                dias_alugados=dias
            )
            self.repo.salvar_emprestimo(novo_emprestimo)
            equip.disponivel = False
            self.notificador.notificar_emprestimo(email, date.today() + timedelta(days=dias))
            return True
        return False