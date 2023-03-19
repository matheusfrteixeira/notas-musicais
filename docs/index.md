![logo_do_projeto](assets/logo.png){width="300" .center}
# Notas musicais


## Como usar?

Você pode chamar as escalas via linha de comando. Por Exemplo:

```bash
poetry run escalas
```

Retornando os graus e as notas correnpondentes a essa escala:

```
┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━┓
┃ I ┃ II ┃ III ┃ IV ┃ V ┃ VI ┃ VII ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━┩
│ C │ D  │ E   │ F  │ G │ A  │ B   │
└───┴────┴─────┴────┴───┴────┴─────┘
```

### Alteração na escala

O Primero parâmetro do CLI é a tônica da escala que deseja exibir. Desta forma, você pode alterar a escala retornada. Por exemplo, a escala de F#:

```bash
poetry run escalas F#
```

## Alteração na tonalidade da escala

Você pode alterar a tonalidade da escala também como segundo parâmetro, exmeplo na escala de `D#` maior:

```
poetry run escalas D# maior

┏━━━━┳━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ I  ┃ II ┃ III ┃ IV ┃ V  ┃ VI ┃ VII ┃
┡━━━━╇━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ D# │ F  │ G   │ G# │ A# │ C  │ D   │
└────┴────┴─────┴────┴────┴────┴─────┘
```

## Mais informalções sobre o CLI

Para descobrir outras opções execute a flag `--help`:
```bash
poetry run escalas --help

 Usage: escalas [OPTIONS] [TONICA] [TONALIDADE]

╭─ Arguments ──────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│   tonica          [TONICA]      Tônica da escala [default: C]                                                        │
│   tonalidade      [TONALIDADE]  Tonalidade da escala [default: maior]                                                │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```