![logo_do_projeto](assets/logo.png){width="300" .center}
# Notas musicais

Notas musicais é um CLI para ajudar na formação de escalas e acordes

Temos dois comandos disponíveis: `escala` e `acorde`

{% include "templates/cards.html" %}

{% include "templates/instalacao.md" %}

## Como usar?

### Escalas

Você pode chamar as escalas via linha de comando. Por Exemplo:

```bash
{{commands.run}} escala
```

Retornando os graus e as notas correnpondentes a essa escala:

```
┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━┓
┃ I ┃ II ┃ III ┃ IV ┃ V ┃ VI ┃ VII ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━┩
│ C │ D  │ E   │ F  │ G │ A  │ B   │
└───┴────┴─────┴────┴───┴────┴─────┘
```

#### Alteração na escala

O Primero parâmetro do CLI é a tônica da escala que deseja exibir. Desta forma, você pode alterar a escala retornada. Por exemplo, a escala de F#:

```bash
{{commands.run}}  escala F#
```

#### Alteração na tonalidade da escala

Você pode alterar a tonalidade da escala também como segundo parâmetro, exmeplo na escala de `D#` maior:

```
{{commands.run}}  escala D# menor

┏━━━━┳━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ I  ┃ II ┃ III ┃ IV ┃ V  ┃ VI ┃ VII ┃
┡━━━━╇━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ D# │ F  │ F#  │ G# │ A# │ B  │ C#  │
└────┴────┴─────┴────┴────┴────┴─────┘
```

## Acordes

Uso básico
```bash
{{commands.run}}  acorde
┏━━━┳━━━━━┳━━━┓
┃ I ┃ III ┃ V ┃
┡━━━╇━━━━━╇━━━┩
│ C │ E   │ G │
└───┴─────┴───┘
```

### Variações na cifra

```bash
{{commands.run}}  acorde C+
┏━━━┳━━━━━┳━━━━┓
┃ I ┃ III ┃ V+ ┃
┡━━━╇━━━━━╇━━━━┩
│ C │ E   │ G# │
└───┴─────┴────┘
```

Até o momento você pode usar acordes maiores, menores, diminuto e aumentados

## Mais informalções sobre o CLI

Para descobrir outras opções execute a flag `--help`:
```bash
{{commands.run}}  --help

 Usage: escalas [OPTIONS] [TONICA] [TONALIDADE]

╭─ Arguments ──────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│   tonica          [TONICA]      Tônica da escala [default: C]                                                        │
│   tonalidade      [TONALIDADE]  Tonalidade da escala [default: maior]                                                │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```