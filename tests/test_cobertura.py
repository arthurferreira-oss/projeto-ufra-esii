from datetime import date, timedelta
from app.sistema import SistemaDeEmprestimos
from services.evento import Evento


def test_sistema_fachada_fluxo_completo():
    sistema = SistemaDeEmprestimos()

    # Testa os métodos principais da fachada
    assert sistema.registrar(1, "Ana", "ana@ufra.edu.br", 7) is True
    assert sistema.registrar(1, "Pedro", "pedro@ufra.edu.br", 7) is False

    # Devolução
    sistema.devolver(1)


def test_notificador_metodos_conveniencia():
    from services.notificador import Notificador

    notificador = Notificador()
    hoje = date.today()
    devolucao = hoje + timedelta(days=7)

    notificador.notificar_emprestimo("teste@ufra.edu.br", devolucao)
    notificador.notificar_devolucao("teste@ufra.edu.br", 10.0)
    notificador.notificar_atraso("teste@ufra.edu.br")


def test_evento_getitem():
    evento = Evento(tipo="emprestimo", email="ana@ufra.edu.br", multa=5.0)
    assert evento[0] == "emprestimo"
    assert evento["email"] == "ana@ufra.edu.br"