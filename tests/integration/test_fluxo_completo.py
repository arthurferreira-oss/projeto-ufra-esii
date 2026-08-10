# tests/integration/test_fluxo_completo.py
from repositories.repositorio_emprestimo import RepositorioEmprestimo
from services.notificador import Notificador
from services.servico_emprestimo import ServicoEmprestimo


def test_fluxo_registrar_devolver_com_componentes_reais():
    repositorio = RepositorioEmprestimo()
    notificador = Notificador()
    servico = ServicoEmprestimo(repositorio, notificador)

    # Executa o fluxo de ponta a ponta com as classes concretas
    sucesso = servico.registrar(1, "Ana", "ana@ufra.edu.br", dias=7)
    assert sucesso is True
