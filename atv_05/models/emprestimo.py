from dataclasses import dataclass
from datetime import date

@dataclass
class Emprestimo:
    id: int
    equip_id: int
    nome_usuario: str
    email_usuario: str
    data_emprestimo: date
    dias_alugados: int