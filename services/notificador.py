# services/notificador.py
import datetime
from services.interfaces import INotificador

class Notificador(INotificador):
    def notificar_emprestimo(self, email: str, data_devolucao: datetime.date) -> None:
        print(f"[Notificação] Empréstimo registrado para {email}. Devolução: {data_devolucao}")

    def notificar_devolucao(self, email: str, multa: float) -> None:
        print(f"[Notificação] Equipamento devolvido por {email}. Multa calculada: R$ {multa:.2f}")

    def notificar_atraso(self, email: str) -> None:
        print(f"[Notificação] Alerta enviado para {email}: Seu empréstimo está atrasado!")