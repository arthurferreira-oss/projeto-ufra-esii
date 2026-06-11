from models.equipamento import Equipamento, Notebook, Projetor, Cabo

class FabricaEquipamento:
    _registro = {
        "notebook": Notebook,
        "projetor": Projetor,
        "cabo": Cabo,
    }

    @classmethod
    def criar(cls, tipo: str, id: int, nome: str) -> Equipamento:
        classe = cls._registro.get(tipo)
        if classe is None:
            raise ValueError(f"Tipo desconhecido: {tipo}")
        # Retorna a instância correta passando os parâmetros na ordem da dataclass
        return classe(id, nome, tipo)