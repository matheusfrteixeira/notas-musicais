"""
AAA - Arrange - Act - Assets!
"""
from pytest import mark, raises

from notas_musicais.escalas import ESCALAS, NOTAS, escalas


def test_escala_deve_funcionar_com_notas_minusculas():
    # Arrange - Arrumar os dados do Teste
    tonica = 'c'
    tonalidade = 'maior'

    # Act
    result = escalas(tonica, tonalidade)

    assert result


def test_escala_deve_retornar_um_erro_dizendo_que_a_nota_nao_existe():
    tonica = 'X'
    tonalidade = 'maior'

    mensagme_de_erro = f'Essa nota não existe, tente uma dessas {NOTAS}'

    with raises(ValueError) as error:
        escalas(tonica, tonalidade)

    assert mensagme_de_erro == error.value.args[0]


def test_deve_retornar_que_escala_n_existe():
    tonica = 'C'
    tonalidade = 'tonalidade'

    mensagme_de_erro = f'Escala não existe ou não foi implementada, tente uma dessas {list(ESCALAS.keys())}'

    with raises(KeyError) as error:
        escalas(tonica, tonalidade)

    assert mensagme_de_erro == error.value.args[0]


@mark.parametrize(
    'tonica, tonalidade, esperado',
    [
        ('C', 'maior', ['C', 'D', 'E', 'F', 'G', 'A', 'B']),
        ('C#', 'maior', ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C']),
        ('F', 'maior', ['F', 'G', 'A', 'A#', 'C', 'D', 'E']),
        ('C', 'menor', ['C', 'D', 'D#', 'F', 'G', 'G#', 'A#']),
        ('C#', 'menor', ['C#', 'D#', 'E', 'F#', 'G#', 'A', 'B']),
        ('F', 'menor', ['F', 'G', 'G#', 'A#', 'C', 'C#', 'D#']),
    ],
)
def test_deve_retornar_as_notas_corretas(tonica, tonalidade, esperado):
    resultado = escalas(tonica, tonalidade)
    assert resultado['notas'] == esperado


def test_deve_retornar_graus_um_a_sete():
    esperado = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']

    assert escalas('C', 'maior')['graus'] == esperado
