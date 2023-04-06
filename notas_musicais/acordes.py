from notas_musicais.escalas import NOTAS, escalas


def _menor(cifra):
    nota = cifra.split('m')[0]
    if '+' in cifra:
        tonica, terca, quinta = triade(nota, 'menor')
        notas = [tonica, terca, semitom(quinta, intervalo=+1)]
        graus = ['I', 'III-', 'V+']
    else:
        notas = triade(nota, 'menor')
        graus = ['I', 'III-', 'V']

    return notas, graus


def semitom(nota, *, intervalo):
    pos = NOTAS.index(nota) + intervalo

    return NOTAS[pos % 12]


def triade(nota, tonalidade):
    graus = (0, 2, 4)
    notas_da_escala, _ = escalas(nota, tonalidade).values()

    return [notas_da_escala[grau] for grau in graus]


def acorde(cifra):
    """
    Examples:
        >>> acorde('C')
        {'notas': ['C', 'E', 'G'], 'graus': ['I', 'III', 'V']}
    """

    if 'm' in cifra:
        notas, graus = _menor(cifra)

    elif '°' in cifra:
        nota = cifra.split('°')[0]
        tonica, terca, quinta = triade(nota, 'menor')
        notas = [tonica, terca, semitom(quinta, intervalo=-1)]
        graus = ['I', 'III-', 'V-']

    elif '+' in cifra:
        nota = cifra.split('+')[0]
        tonica, terca, quinta = triade(nota, 'maior')
        notas = [tonica, terca, semitom(quinta, intervalo=+1)]
        graus = ['I', 'III', 'V+']

    else:
        notas = triade(cifra, 'maior')
        graus = ['I', 'III', 'V']

    return {'notas': notas, 'graus': graus}
