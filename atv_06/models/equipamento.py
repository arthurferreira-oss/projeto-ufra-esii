from abc import ABC, abstractmethod

class Equipamento(ABC):
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    @abstractmethod
    def calcular_multa(self, dias_atraso) -> float:
        pass

class Notebook(Equipamento):
    def calcular_multa(self, dias_atraso) -> float:
        # Exemplo: R$ 5,00 por dia
        return max(0.0, dias_atraso * 5.0)

class Projetor(Equipamento):
    def calcular_multa(self, dias_atraso) -> float:
        # Exemplo: R$ 10,00 por dia
        return max(0.0, dias_atraso * 10.0)