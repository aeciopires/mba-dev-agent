# Como contribuir

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

## Fluxo de contribuição

1. Verifique se a proposta está alinhada ao propósito educacional do
   repositório. Para mudanças maiores, abra uma issue ou discussão antes de
   começar, quando possível.
2. Crie uma branch dedicada à alteração.
3. Faça mudanças focadas, seguindo os padrões existentes e mantendo a
   compatibilidade com as versões de Python e Google ADK declaradas no projeto.
4. Atualize a documentação relacionada sempre que o comportamento, os
   requisitos ou os passos de uso mudarem.
5. Revise e valide as alterações antes de abrir um pull request.

## Boas práticas

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

Antes de enviar a contribuição, confira também:

```bash
git diff --check
git status --short
```

## Pull requests

Ao abrir um pull request:

- explique o problema ou objetivo e resuma a solução;
- indique os arquivos ou agentes afetados;
- informe os comandos de validação executados e os resultados;
- inclua ou atualize a documentação pertinente;
- mantenha a alteração focada e não inclua arquivos locais, ambientes virtuais
  ou segredos.

Contribuições estão sujeitas aos termos da licença GPLv3 deste repositório.
