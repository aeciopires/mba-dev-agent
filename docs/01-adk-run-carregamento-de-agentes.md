<!-- TOC --->

- [Como o `adk run` carrega o agente](#como-o-adk-run-carrega-o-agente)
  - [A regra de ouro](#a-regra-de-ouro)
  - [Estrutura mínima](#estrutura-mínima)
  - [Ordem de busca do loader](#ordem-de-busca-do-loader)
  - [Regras de nome](#regras-de-nome)
  - [Erros comuns](#erros-comuns)
  - [Bônus: o que mais a pasta ancora](#bônus-o-que-mais-a-pasta-ancora)

<!-- TOC --->


# Como o `adk run` carrega o agente

> ADK Python 2.11.0 · `adk run`, `adk web` e `adk api_server` usam o mesmo mecanismo.

## A regra de ouro

O `adk run` recebe uma **pasta**, não um arquivo. Ele **importa** o módulo com o
nome da pasta e procura, no nível do módulo, uma variável chamada:

1. `app` (instância de `App`), ou
2. `root_agent` (instância de `BaseAgent`)

Nada de varrer arquivos: a busca é por esses dois nomes exatos.

## Estrutura mínima

```text
src/
└── meu_agente1/            ← nome da pasta = app_name (sessões, adk web)
    ├── __init__.py        ← pode ser vazio
    ├── agent.py           ← define root_agent
    └── .env               ← carregado automaticamente antes do import
```

```python
# meu_agente1/agent.py
from google.adk.agents import Agent

root_agent = Agent(
    name="meu_agente1",                # obrigatório (único campo obrigatório)
    model="gemini-2.5-flash",
    instruction="Você é um assistente...",
)
```

```bash
# rode do diretório PAI da pasta do agente
cd src/meu_agente1/
adk run .
```

## Ordem de busca do loader

| Ordem | O que tenta | Equivale a |
|---|---|---|
| 1 | `import meu_agente1` | `root_agent` no `__init__.py` |
| 2 | `import meu_agente1.agent` | `root_agent` no `agent.py` ← o padrão |
| 3 | `meu_agente1/root_agent.yaml` | agente declarativo (experimental) |

Os demais arquivos da pasta (`subagents/`, `tools/`...) só são carregados se o
`agent.py` os **importar** — direta ou indiretamente.

## Regras de nome

- **Pasta**: só letras, dígitos e `_` (`acme_support` ✅, `acme-support` ❌).
- **Campo `name` do Agent**: identificador Python válido; `"user"` é proibido;
  único entre os agentes da árvore.
- Pasta e `name` **não precisam** ser iguais, mas por convenção deixe iguais.

## Erros comuns

| Erro | Causa provável | Correção |
|---|---|---|
| `No root_agent found` | `root_agent` não está no nível do módulo | Defina `root_agent = Agent(...)` no topo do `agent.py` |
| Hint "running from inside an agent directory" | Rodou de dentro da pasta do agente | Rode do diretório pai |
| `Invalid agent name` | Pasta com hífen ou espaço | Renomeie para `snake_case` |
| Subagente/tool "não existe" | Arquivo nunca importado | Confira a cadeia de imports a partir do `agent.py` |

## Bônus: o que mais a pasta ancora

- **`.env`** — carregado antes do seu código rodar.
- **`app_name`** — chave das sessões persistidas e do seletor do `adk web`.
- **Multi-agente** — `adk web pasta_pai/` lista cada subpasta como um agente.