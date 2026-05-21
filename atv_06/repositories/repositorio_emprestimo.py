from models.equipamento import Notebook, Projetor

# Exemplo de como deve ficar a lógica de criação:
def criar_equipamento(id, nome, tipo):
    if tipo == "Notebook":
        return Notebook(id, nome)
    elif tipo == "Projetor":
        return Projetor(id, nome)
    # Se houver outros tipos futuramente, você adiciona aqui.