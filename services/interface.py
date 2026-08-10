# services/interfaces.py
import datetime
from abc import ABC, abstractmethod


class INotificador(ABC):
    @abstractmethod
    def notificar_emprestimo(self, email: str, data_devolucao: datetime.date) -> None:
        pass

    @abstractmethod
    def notificar_devolucao(self, email: str, multa: float) -> None:
        pass

    @abstractmethod
    def notificar_atraso(self, email: str) -> None:
        pass
