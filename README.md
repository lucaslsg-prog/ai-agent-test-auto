# Como executar os testes

Este projeto contém exemplos em Python para cálculo de desconto e priorização de chamados, com testes automatizados usando `pytest`.

## Estrutura esperada

```text
ai-agent-test-auto/
├── requirements.txt
├── discount.py
├── test_discount.py
├── ticket_prioritization.py
└── test_ticket_prioritization.py
```

## 1. Acessar o diretório do projeto

No Prompt de Comando do Windows:

```cmd
cd C:\Users\mnslgonc\ai-agent-test-auto
```

## 2. Instalar as dependências

Execute:

```cmd
pip install -r requirements.txt
```

O arquivo `requirements.txt` deve conter:

```text
pytest>=8.0,<9.0
```

## 3. Executar os testes

Como o comando `pytest` pode não estar disponível diretamente no `PATH` do Windows, execute-o através do Python:

```cmd
python -m pytest test_discount.py -v
```

Para executar todos os testes encontrados no projeto:

```cmd
python -m pytest -v
```

## 4. Resultado esperado

Com todos os cenários funcionando corretamente, o resumo da execução deverá indicar que os cinco testes passaram:

```text
5 passed
```

Os cenários verificados são:

- desconto padrão de 8%;
- desconto de 0%;
- desconto limite de 100%;
- valor negativo, que deve gerar `ValueError`;
- percentual acima de 100%, que deve gerar `ValueError`.

## 5. Executar apenas um teste

Também é possível executar somente um caso específico. Por exemplo:

```cmd
python -m pytest test_discount.py::test_standard_discount -v
```

## Arquivo `test_discount.py`

O arquivo de testes deve importar a função do arquivo `discount.py`:

```python
import pytest

from discount import calculate_discount


def test_standard_discount():
    assert calculate_discount(12500, 8) == 11500.00


def test_zero_discount():
    assert calculate_discount(999, 0) == 999.00


def test_full_discount():
    assert calculate_discount(999, 100) == 0.00


def test_negative_amount():
    with pytest.raises(ValueError):
        calculate_discount(-100, 10)


def test_discount_above_limit():
    with pytest.raises(ValueError):
        calculate_discount(1000, 101)
```

## Comando rápido

Se as dependências já estiverem instaladas, basta executar:

```cmd
python -m pytest -v
```

## Priorização de chamados

A função `prioritize_tickets` recebe uma sequência de chamados, cada um como um
dicionário com o campo `priority`. Os valores reconhecidos são `alta`, `média`
e `baixa`, sem distinção entre maiúsculas/minúsculas e espaços ao redor. O
resultado contém chamados reconhecidos em ordem de prioridade, mantendo a ordem
de chegada entre prioridades iguais, e uma lista separada de prioridades
desconhecidas.

```python
from ticket_prioritization import prioritize_tickets

chamados = [
    {"id": "CH-001", "priority": "baixa"},
    {"id": "CH-002", "priority": "alta"},
    {"id": "CH-003", "priority": "média"},
    {"id": "CH-004", "priority": "a definir"},
]

resultado = prioritize_tickets(chamados)
```

Neste exemplo fictício, `CH-002`, `CH-003` e `CH-001` aparecem em
`resultado.ordered_tickets`; `CH-004` aparece em
`resultado.unknown_priority_tickets` para sinalização, sem receber uma
prioridade presumida.
