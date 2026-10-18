# Requisitos de software

Este documento descreve como preparar o ambiente de desenvolvimento do
`mba-dev-agent` em português (pt-BR).

## Sumário

<!-- TOC -->

- [Requisitos de software](#requisitos-de-software)
  - [Sumário](#sumário)
  - [Sistemas operacionais e arquiteturas](#sistemas-operacionais-e-arquiteturas)
  - [Softwares necessários](#softwares-necessários)
  - [Ubuntu](#ubuntu)
    - [1. Instalar Git, curl e dependências de compilação](#1-instalar-git-curl-e-dependências-de-compilação)
    - [2. Instalar mise e uv](#2-instalar-mise-e-uv)
  - [macOS](#macos)
    - [1. Instalar as ferramentas de linha de comando do Xcode](#1-instalar-as-ferramentas-de-linha-de-comando-do-xcode)
    - [2. Instalar Homebrew, mise, uv e bibliotecas de compilação](#2-instalar-homebrew-mise-uv-e-bibliotecas-de-compilação)
  - [Ativar o autocomplete do mise](#ativar-o-autocomplete-do-mise)
  - [Instalação das dependências do projeto](#instalação-das-dependências-do-projeto)
  - [Verificação](#verificação)
<!-- TOC -->

## Sistemas operacionais e arquiteturas

| Sistema operacional | Arquitetura |
| --- | --- |
| Ubuntu 22.04, 24.04 e 26.04 | amd64 (x86_64) |
| macOS | amd64 (Intel) e arm64 (Apple Silicon) |

## Softwares necessários

- **Git** para obter o código-fonte do projeto.
- **mise** para instalar e selecionar a versão de Python declarada em
  [`mise.toml`](./mise.toml).
- **Python 3.14**, conforme configurado pelo projeto.
- **uv** para sincronizar as dependências declaradas em `pyproject.toml` e
  `uv.lock`.
- No Ubuntu, compilador e bibliotecas de desenvolvimento usados pelo mise ao
  instalar Python.
- No macOS, as ferramentas de linha de comando do Xcode e o Homebrew.

O pacote `google-adk` é instalado no ambiente virtual do projeto pelo `uv`;
não é necessário instalá-lo globalmente.

## Ubuntu

Os comandos a seguir atendem Ubuntu 22.04, 24.04 e 26.04 em amd64.

### 1. Instalar Git, curl e dependências de compilação

```bash
sudo apt update
sudo apt install -y \
  build-essential \
  curl \
  git \
  libbz2-dev \
  libffi-dev \
  libgdbm-compat-dev \
  libgdbm-dev \
  liblzma-dev \
  libncurses-dev \
  libreadline-dev \
  libsqlite3-dev \
  libssl-dev \
  pkg-config \
  tk-dev \
  uuid-dev \
  xz-utils \
  zlib1g-dev
```

### 2. Instalar mise e uv

```bash
curl https://mise.run | sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Os instaladores colocam os executáveis em `~/.local/bin`. Se esse diretório ainda
não estiver no `PATH`, adicione-o à configuração do shell (por exemplo,
`~/.bashrc` ou `~/.zshrc`) e abra um novo terminal:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

## macOS

Os passos abaixo atendem Macs Intel (amd64) e Apple Silicon (arm64).

### 1. Instalar as ferramentas de linha de comando do Xcode

Se ainda não estiverem instaladas, execute:

```bash
xcode-select --install
```

Conclua a instalação na janela exibida.

### 2. Instalar Homebrew, mise, uv e bibliotecas de compilação

Caso ainda não tenha o Homebrew, instale-o seguindo as instruções em
[brew.sh](https://brew.sh/). Em seguida, execute:

```bash
brew install mise uv openssl@3 readline sqlite xz zlib tcl-tk
```

## Ativar o autocomplete do mise

O mise pode instalar as definições de autocomplete para o shell usado no
terminal. Execute **um** dos comandos abaixo, conforme seu shell:

```bash
# Bash (comum no Ubuntu)
mise completion bash --install

# Zsh (padrão no macOS)
mise completion zsh --install
```

Se o comando indicar uma linha adicional de configuração para o shell, siga a
instrução exibida. Depois, abra um novo terminal ou reinicie o shell para que o
autocomplete fique disponível. Consulte também a documentação de
[autocomplete do mise](https://mise.jdx.dev/shell-setup.html#autocompletion).

## Instalação das dependências do projeto

Na raiz do repositório, instale a versão de Python e sincronize o ambiente virtual
com o arquivo de lock:

```bash
mise install
mise exec -- uv sync --locked
```

O comando `uv sync --locked` instala as versões registradas em `uv.lock` e
falha se o arquivo de lock estiver desatualizado em relação ao projeto.

## Verificação

Execute na raiz do repositório:

```bash
mise exec -- python --version
mise exec -- uv run adk --version
```

O primeiro comando deve informar Python 3.14. O segundo confirma que o comando
`adk`, fornecido pela dependência `google-adk`, está disponível no ambiente do
projeto.
