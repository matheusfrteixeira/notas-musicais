"""
Modulo das escalas

Attributes:
    ESCALAS: Escalas implementadas usnado a notação de inteiros
    NOTAS: Notas musicais

# Escalas

# Notas
"""

NOTAS = 'C C# D D# E F F# G G# A A# B'.split()
ESCALAS = {'maior': (0, 2, 4, 5, 7, 9, 11), 'menor': (0, 2, 3, 5, 7, 8, 10)}


def escalas(tonica: str, tonalidade: str) -> dict[str, list[str]]:
    """
    Gera uma escala apartir de uma tônica e uma tonalidade.

    Parameters:
        tonica: Nota que será a tônica da escala
        tonalidade: Tonalidade da escala
    Returns:
        Um dicionário com as notas da escala e os graus

    Raises:
        ValueErro: Caso a tônica não seja uma nota valida.
        KeyError: Caso a escala não exista ou não tenha sido impementada.

    Examples:
        >>> escalas('C', 'maior')
        {'notas': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

        >>> escalas('a', 'menor')
        {'notas': ['A', 'B', 'C', 'D', 'E', 'F', 'G'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    """
    tonica = tonica.upper()
    try:
        intervalos = ESCALAS[tonalidade]
        tonica_pos = NOTAS.index(tonica)
    except ValueError:
        raise ValueError(f'Essa nota não existe, tente uma dessas {NOTAS}')
    except KeyError:
        raise KeyError(
            f'Escala não existe ou não foi implementada, tente uma dessas {list(ESCALAS.keys())}'
        )

    temp = []

    for intervalo in intervalos:
        nota = (tonica_pos + intervalo) % 12
        temp.append(NOTAS[nota])

    return {'notas': temp, 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
