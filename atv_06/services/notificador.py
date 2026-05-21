# Responsabilidade: Notificar usuários sobre eventos do sistema.
class Notificador:
    def notificar_emprestimo(self, email: str, data_devolucao):
        print(f"[EMAIL] Notificação enviada para {email}: Devolução prevista para {data_devolucao}")