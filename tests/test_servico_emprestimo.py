import datetime

import pytest


def test_registrar_devolve_true_quando_equipamento_disponivel(servico):
    assert servico.registrar(1, "Ana", "ana@x.com", 7) is True


def test_registrar_devolve_false_quando_equipamento_indisponivel(
    servico, repositorio_fake
):
    repositorio_fake.marcar_indisponivel(1)
    assert servico.registrar(1, "Ana", "ana@x.com", 7) is False


def test_registrar_notifica_usuario_apos_sucesso(servico, notificador_spy):
    servico.registrar(1, "Ana", "ana@x.com", 7)
    assert len(notificador_spy.eventos) == 1
    assert notificador_spy.eventos[0][0] == "emprestimo"


@pytest.mark.parametrize(
    "equip_id, dias_atraso, multa_esperada",
    [(1, 3, 30.0), (1, 1, 10.0), (2, 2, 30.0), (2, 4, 60.0), (3, 5, 10.0), (3, 1, 2.0)],
)
def test_devolver_calcula_multa_correta_para_atraso(
    servico, repositorio_fake, notificador_spy, equip_id, dias_atraso, multa_esperada
):
    servico.registrar(equip_id, "Ana", "ana@x.com", 7)
    emp = repositorio_fake.buscar_emprestimo(1)
    emp.data_devolucao = datetime.date.today() - datetime.timedelta(days=dias_atraso)

    servico.devolver(1)
    evento = next((e for e in notificador_spy.eventos if e[0] == "devolucao"), None)
    assert evento is not None
    assert evento[2] == multa_esperada
