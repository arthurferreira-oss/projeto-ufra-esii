# models/equipamento.py
from abc import ABC, abstractmethod


class Equipamento(ABC):
    def __init__(self, id: int, nome: str, tipo: str):
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.disponivel = True

    @abstractmethod
    def calcular_multa(self, dias: int) -> float:
        pass


class Notebook(Equipamento):
    def calcular_multa(self, dias: int) -> float:
        return max(0.0, dias * 10.0)


class Projetor(Equipamento):
    def calcular_multa(self, dias: int) -> float:
        return max(0.0, dias * 15.0)


class Cabo(Equipamento):
    def calcular_multa(self, dias: int) -> float:
        return max(0.0, dias * 2.0)
