# models/emprestimo.py
import datetime

class Emprestimo:
    def __init__(self, id: int, equipamento_id: int, usuario: str, email: str, data_emprestimo: datetime.date, data_devolucao: datetime.date):
        self.id = id
        self.equipamento_id = equipamento_id
        self.usuario = usuario
        self.email = email
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao
        self.devolvido = False