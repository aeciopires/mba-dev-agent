# mba-dev-agent

Repositório de estudos e exemplos práticos de desenvolvimento de agentes de IA,
criados durante a disciplina de desenvolvimento de agentes do MBA. Os exemplos
usam o [Google Agent Development Kit (ADK)](https://adk.dev/) com Python e servem
como material didático para explorar a criação, a execução e a organização de
agentes.

> Os agentes e dados incluídos são exemplos didáticos. Não use credenciais,
> dados de clientes ou as ferramentas demonstrativas em um ambiente de produção.

<!-- TOC -->

- [mba-dev-agent](#mba-dev-agent)
  - [Objetivo](#objetivo)
  - [Estrutura do repositório](#estrutura-do-repositório)
  - [Requisitos e instalação](#requisitos-e-instalação)
  - [Executar os agentes](#executar-os-agentes)
  - [Documentação](#documentação)
  - [Como contribuir](#como-contribuir)
  - [Referências](#referências)
  - [Desenvolvedor](#desenvolvedor)
  - [Licença](#licença)

<!-- TOC -->

## Objetivo

O projeto reúne exemplos pequenos e materiais de apoio para aprender a
desenvolver agentes com o Google ADK.

## Estrutura do repositório

```text
.
├── docs/                 # reúne tutoriais e notas técnicas do projeto
│   └── 01-adk-run-carregamento-de-agentes.md
├── src/
│   ├── meu_agente1/
│   │   ├── __init__.py
│   │   └── agent.py      # contém o exemplo mínimo de agente
│   └── meu_agente2/
│       ├── __init__.py
│       └── agent.py      # contém o agente de atendimento e suas ferramentas demonstrativas
├── .env.example          # serve de referência para variáveis de ambiente. Crie seu
                          # arquivo local de configuração a partir dele quando necessário; nunca adicione chaves ou # outros segredos ao controle de versão
├── mise.toml             # define a versão dos softwares usados no repositório
├── pyproject.toml        # declara os metadados, a versão mínima de Python e as dependências do projeto
├── REQUIREMENTS.md       # descreve os softwares necessários e as instruções de instalação
└── uv.lock               # registra as versões resolvidas das dependências do projeto
```

## Requisitos e instalação

Consulte [Requisitos de software](./REQUIREMENTS.md) para as instruções completas
de instalação no Ubuntu e macOS. Com `mise` e `uv` instalados, prepare o ambiente
na raiz do repositório:

```bash
mise install
uv init .
```

Para executar os agentes que usam o modelo Gemini, configure uma chave válida da
Google AI Studio de forma local. Não compartilhe nem versione essa credencial.

## Executar os agentes

Execute os comandos na raiz do repositório:

```bash
source .venv/bin/activate  # ativa o ambiente virtual
uv run adk run src/meu_agente1
uv run adk run src/meu_agente2
```

O ADK também oferece uma interface web. Para carregar os agentes do diretório
`src/`, execute:

```bash
uv run adk web src
```

## Documentação

- [Como o `adk run` carrega o agente](./docs/01-adk-run-carregamento-de-agentes.md)
- [Requisitos de software e instalação](./REQUIREMENTS.md)

## Como contribuir

Contribuições são bem-vindas. Antes de abrir uma alteração, consulte
[CONTRIBUTING.md](./CONTRIBUTING.md) para orientações de desenvolvimento,
validação e envio de contribuições.

## Referências

- [Projeto da disciplina](https://github.com/devfullcycle/mba-ia-dev-agents)
- [Documentação do Google ADK](https://adk.dev/)
- [Google ADK para Python](https://github.com/google/adk-python)
- [Repositório de documentação do ADK](https://github.com/google/adk-docs)

## Desenvolvedor

- Aécio Pires — [Linktree](https://linktr.ee/aeciopires)

## Licença

GPLv3. Consulte o arquivo [LICENSE](./LICENSE) para mais detalhes.
