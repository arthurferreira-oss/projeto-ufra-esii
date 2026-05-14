# Responsabilidade: Armazenar e recuperar dados de empréstimos e equipamentos.
from models.equipamento import Equipamento
from models.emprestimo import Emprestimo

# atv_04/repositories/repositorio_emprestimo.py

class RepositorioEmprestimo:
    def __init__(self):
        # Substitua as listas vazias por estas com dados de teste:
        self.equipamentos = [
            Equipamento(id=1, nome="Projetor", disponivel=True),
            Equipamento(id=2, nome="Notebook", disponivel=True)
        ]
        self.emprestimos = []

    # Mantenha o restante dos métodos (buscar_equipamento e salvar_emprestimo) como estão

    def buscar_equipamento(self, equip_id: int):
        return next((e for e in self.equipamentos if e.id == equip_id), None)

    def salvar_emprestimo(self, emprestimo: Emprestimo):
        self.emprestimos.append(emprestimo)