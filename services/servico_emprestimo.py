# services/servico_emprestimo.py
import datetime
from repositories.interfaces import IRepositorioEmprestimo
from services.interfaces import INotificador
from models.emprestimo import Emprestimo

class ServicoEmprestimo:
    def __init__(self, repositorio: IRepositorioEmprestimo, notificador: INotificador):
        self.repositorio = repositorio
        self.notificador = notificador

    def registrar(self, equipamento_id: int, usuario: str, email: str, dias: int) -> bool:
        equipamento = self.repositorio.buscar_equipamento(equipamento_id)
        if not equipamento or not equipamento.disponivel:
            return False
            
        hoje = datetime.date.today()
        data_devolucao = hoje + datetime.timedelta(days=dias)
        
        novo_emprestimo = Emprestimo(
            id=self.repositorio.proximo_id_emprestimo(),
            equipamento_id=equipamento_id,
            usuario=usuario,
            email=email,
            data_emprestimo=hoje,
            data_devolucao=data_devolucao
        )
        
        self.repositorio.salvar_emprestimo(novo_emprestimo)
        self.repositorio.marcar_indisponivel(equipamento_id)
        self.notificador.notificar_emprestimo(email, data_devolucao)
        return True

    def devolver(self, emprestimo_id: int) -> None:
        emprestimo = self.repositorio.buscar_emprestimo(emprestimo_id)
        if not emprestimo or emprestimo.devolvido:
            return

        hoje = datetime.date.today()
        multa = 0.0
        
        if hoje > emprestimo.data_devolucao:
            dias_atraso = (hoje - emprestimo.data_devolucao).days
            equipamento = self.repositorio.buscar_equipamento(emprestimo.equipamento_id)
            if equipamento:
                multa = equipamento.calcular_multa(dias_atraso)

        self.repositorio.marcar_devolvido(emprestimo_id)
        self.repositorio.marcar_disponivel(emprestimo.equipamento_id)
        self.notificador.notificar_devolucao(emprestimo.email, multa)