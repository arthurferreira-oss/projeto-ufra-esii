# repositories/interfaces.py
from abc import ABC, abstractmethod

from models.emprestimo import Emprestimo
from models.equipamento import Equipamento


class IRepositorioEmprestimo(ABC):
    @abstractmethod
    def buscar_equipamento(self, id: int) -> Equipamento | None:
        pass

    @abstractmethod
    def salvar_emprestimo(self, emprestimo: Emprestimo) -> None:
        pass

    @abstractmethod
    def buscar_emprestimo(self, id: int) -> Emprestimo | None:
        pass

    @abstractmethod
    def marcar_indisponivel(self, equip_id: int) -> None:
        pass

    @abstractmethod
    def marcar_disponivel(self, equip_id: int) -> None:
        pass

    @abstractmethod
    def marcar_devolvido(self, emprestimo_id: int) -> None:
        pass

    @abstractmethod
    def listar_em_atraso(self) -> list[Emprestimo]:
        pass

    @abstractmethod
    def proximo_id_emprestimo(self) -> int:
        pass
