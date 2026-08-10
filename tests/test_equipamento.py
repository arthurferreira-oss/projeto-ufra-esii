import pytest

from models.equipamento import Cabo, Notebook, Projetor


@pytest.mark.parametrize(
    "equipamento, dias, multa_esperada",
    [
        (Notebook(1, "Dell", "notebook"), 3, 30.0),
        (Projetor(2, "Epson", "projetor"), 2, 30.0),
        (Cabo(3, "HDMI", "cabo"), 5, 10.0),
    ],
)
def test_calcular_multa_atraso_positivo(equipamento, dias, multa_esperada):
    assert equipamento.calcular_multa(dias) == multa_esperada
