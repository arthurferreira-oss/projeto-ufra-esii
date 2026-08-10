from dataclasses import dataclass
from datetime import date


@dataclass
class Evento:
    tipo: str
    email: str
    data: date | None = None
    multa: float | None = None

    def __getitem__(self, item):
        """Compatibilidade com testes legados que leem como dicionario/tupla."""
        if item == 0 or item == "tipo":
            return self.tipo
        if item == 1 or item == "email":
            return self.email
        if item == 2 or item == "data":
            return self.data
        if item == 3 or item == "multa":
            return self.multa
        raise KeyError(f"Chave ou índice inválido: {item}")