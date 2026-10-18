# Como contribuir

<!-- TOC -->

- [Como contribuir](#como-contribuir)
  - [Preparar o ambiente](#preparar-o-ambiente)
  - [Boas práticas](#boas-práticas)
  - [Validação](#validação)
  - [Fluxo de commits e pull requests](#fluxo-de-commits-e-pull-requests)

<!-- TOC -->

Obrigado por contribuir com este repositório de estudos e exemplos do Google
ADK. Estas orientações ajudam a manter as contribuições claras, reproduzíveis
e adequadas ao objetivo didático do projeto.

## Preparar o ambiente

Siga as instruções de [Requisitos de software](./REQUIREMENTS.md) para instalar
as ferramentas no seu sistema. Na raiz do repositório, instale Python e as
dependências travadas:

```bash
mise install
mise exec -- uv sync --locked
```

Se a alteração exigir executar um agente com o modelo Gemini, configure
`GOOGLE_API_KEY` localmente. Use `.env.example` como referência, não versione o
arquivo `.env` nem inclua chaves, tokens ou dados pessoais em alterações,
registros de erro ou exemplos.

## Boas práticas

- Verifique se a proposta está alinhada ao propósito educacional do
  repositório.
- Faça mudanças focadas, seguindo os padrões existentes e mantendo a
  compatibilidade com as versões de Python e Google ADK declaradas no projeto.
- Atualize a documentação relacionada sempre que o comportamento, os
  requisitos ou os passos de uso mudarem.
- Revise e valide as alterações antes de abrir um pull request.
- Prefira exemplos pequenos, legíveis e explicados em português (pt-BR).
- Mantenha nomes de pacotes de agente compatíveis com identificadores Python,
  como `meu_agente`; evite espaços e hífens.
- Defina o agente exportado usando o padrão reconhecido pelo ADK, normalmente
  `root_agent`, e documente ferramentas ou configurações necessárias.
- Não inclua credenciais reais, dados sensíveis ou informações pessoais. Use
  valores fictícios nos exemplos.
- Evite apresentar exemplos didáticos como prontos para produção. Destaque
  limitações relevantes de segurança, persistência e tratamento de erros.
- Atualize `uv.lock` quando mudar dependências e mantenha-o consistente com
  `pyproject.toml`.

## Validação

O repositório não define atualmente uma suíte automatizada de testes ou
ferramentas de lint. Para detectar erros de sintaxe em arquivos Python, execute
na raiz do projeto:

```bash
mise exec -- uv run python -m compileall -q src
```

Quando uma alteração afetar o comportamento ou a configuração de um agente,
execute também o agente afetado, conforme os comandos descritos no
[README](./README.md), se tiver as credenciais necessárias. Não inclua a saída
de sessões que contenham dados sensíveis.

## Fluxo de commits e pull requests

Use um fork para propor alterações. Configure a autenticação SSH do GitHub
conforme a [documentação oficial](https://docs.github.com/authentication/connecting-to-github-with-ssh)
e siga estes passos:

1. Crie um fork de `aeciopires/mba-dev-agent` no GitHub e clone-o:

```bash
git clone git@github.com:SEU_USUARIO/mba-dev-agent.git
cd mba-dev-agent
```

2. Registre o repositório original como `upstream` e confira os remotos:

```bash
git remote add upstream git@github.com:aeciopires/mba-dev-agent.git
git remote -v
```

3. Atualize a branch principal local e crie uma branch para sua alteração:

```bash
git switch main
git pull upstream main
git switch -c tipo/descricao-curta
```

   Use um nome simples e descritivo para a branch, por exemplo
   `docs/guia-de-instalacao` ou `fix/carregamento-agente`.

4. Faça e valide as alterações. Revise o diff e confirme que somente os arquivos
   pretendidos serão incluídos:

```bash
git status --short
git diff --check
git diff
```

5. Adicione os arquivos pertinentes, crie commits focados com mensagens
   descritivas e envie a branch ao seu fork:

```bash
git add caminho/do/arquivo
git commit -m "docs: descreve a estrutura do projeto"
git push --set-upstream origin tipo/descricao-curta
```

   Não inclua credenciais, arquivos `.env`, ambientes virtuais nem outros
   arquivos locais no commit. Se houver mais de uma alteração independente,
   prefira separá-las em commits claros.

6. No GitHub, abra um pull request do seu fork para a branch `main` do
   repositório original. Descreva o objetivo, resuma as mudanças e informe as
   validações executadas. Considere e responda às sugestões da revisão; envie
   novos commits à mesma branch quando fizer ajustes.

7. Após o merge, atualize sua branch principal e, se desejar, remova a branch de
   trabalho:

```bash
git switch main
git pull upstream main
git push origin main
git branch -d tipo/descricao-curta
git push origin --delete tipo/descricao-curta
```

Para sincronizar o fork posteriormente, estando na branch `main`, execute:

```bash
git pull upstream main
git push origin main
```

Contribuições estão sujeitas aos termos da licença GPLv3 deste repositório.
