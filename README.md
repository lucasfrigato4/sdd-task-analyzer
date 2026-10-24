# SDD Task Analyzer

Módulo de análise de métricas e produtividade desenvolvido como parte do **Bootcamp III — Análise e Desenvolvimento de Sistemas (CEUB)**.

O projeto utiliza a abordagem **Specification-Driven Development (SDD)**, na qual a especificação e as regras definidas orientam o desenvolvimento, a implementação e a validação do software.

## 📋 Sumário

- [Visão geral](#-visão-geral)
- [Estrutura do projeto](#-estrutura-do-projeto)
- [Tecnologias utilizadas](#-tecnologias-utilizadas)
- [Requisitos](#-requisitos)
- [Execução local](#-execução-local)
- [Testes automatizados](#-testes-automatizados)
- [Execução com Docker](#-execução-com-docker)
- [Docker Compose](#-docker-compose)
- [Integração contínua (CI)](#-integração-contínua-ci)
- [Especificação e regras de contexto](#-especificação-e-regras-de-contexto)
- [Objetivo acadêmico](#-objetivo-acadêmico)

## 🎯 Visão geral

O **SDD Task Analyzer** é um módulo desenvolvido em Python para analisar dados de tarefas e produzir métricas de produtividade conforme as regras definidas para o sistema.

A implementação é orientada por uma especificação documentada e por testes automatizados, permitindo verificar se o comportamento do software está de acordo com os cenários previstos.

O projeto utiliza Docker para executar os testes em um ambiente isolado e GitHub Actions para automatizar sua validação.

## 📁 Estrutura do projeto

```text
sdd-task-analyzer/
├── .github/
│   └── workflows/
│       └── ci.yml
├── specs/
│   └── task_analyzer_spec.md
├── src/
│   └── task_analyzer.py
├── tests/
│   └── test_harness.py
├── .gitignore
├── CONTEXT_RULES.md
├── Dockerfile
├── docker-compose.yml
├── README.md
└── requirements.txt
```

### Descrição dos arquivos

| Arquivo ou diretório | Descrição |
|---|---|
| `.github/workflows/ci.yml` | Configuração do workflow de integração contínua do GitHub Actions. |
| `specs/task_analyzer_spec.md` | Especificação do sistema e comportamento esperado. |
| `src/task_analyzer.py` | Implementação do analisador de tarefas. |
| `tests/test_harness.py` | Testes automatizados para validar o comportamento do sistema. |
| `CONTEXT_RULES.md` | Regras de contexto que orientam o desenvolvimento. |
| `Dockerfile` | Instruções para construir a imagem Docker do projeto. |
| `docker-compose.yml` | Configuração do serviço executado pelo Docker Compose. |
| `requirements.txt` | Dependências Python do projeto. |
| `.gitignore` | Arquivos e diretórios que não devem ser versionados. |

## 🛠️ Tecnologias utilizadas

- **Python 3.11:** linguagem utilizada no desenvolvimento.
- **pytest:** framework utilizado para executar os testes automatizados.
- **Docker:** ferramenta para construir imagens e executar o projeto em contêineres.
- **Docker Compose:** ferramenta para configurar e executar o serviço em contêiner.
- **GitHub Actions:** ferramenta de automação para executar os testes continuamente.
- **Markdown:** formato utilizado na documentação do projeto.

## 📌 Requisitos

### Para execução local

- Python 3.11 ou superior.
- pip para instalação das dependências.

### Para execução com Docker

- Docker Desktop ou Docker Engine.
- Docker Compose.

A execução local exige a instalação do Python e das dependências. Com Docker, as dependências Python são instaladas durante a construção da imagem, conforme as instruções definidas no `Dockerfile`.

## 💻 Execução local

### 1. Clonar o repositório

```bash
git clone https://github.com/lucasfrigato4/sdd-task-analyzer.git
cd sdd-task-analyzer
```

### 2. Criar um ambiente virtual

No Windows:

```powershell
python -m venv .venv
```

No Linux ou macOS:

```bash
python3 -m venv .venv
```

### 3. Ativar o ambiente virtual

No Windows, utilizando PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

No Linux ou macOS:

```bash
source .venv/bin/activate
```

### 4. Instalar as dependências

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## 🧪 Testes automatizados

Os testes estão localizados no arquivo `tests/test_harness.py`.

Para executar a suíte de testes localmente, utilize:

```bash
python -m pytest -v
```

Os cenários automatizados incluem:

- Processamento de dados válidos e cálculo de métricas.
- Tratamento de dados inconsistentes.
- Tratamento de listas vazias.
- Análise de tarefas pendentes.

Na execução realizada durante o desenvolvimento, os quatro testes automatizados foram aprovados.

Exemplo de resultado:

```text
4 passed
```

Esse resultado corresponde à execução registrada durante o desenvolvimento. Caso a implementação ou os testes sejam modificados, o resultado poderá mudar.

## 🐳 Execução com Docker

O Docker permite construir uma imagem com as dependências do projeto e executar os testes em um ambiente isolado.

### 1. Construir a imagem

Na raiz do repositório, execute:

```bash
docker build -t sdd-task-analyzer .
```

### 2. Executar os testes

```bash
docker run --rm sdd-task-analyzer
```

O contêiner executa o comando configurado no `Dockerfile`. Na configuração atual, esse comando inicia o pytest para executar os testes automatizados.

## 🐳 Docker Compose

O arquivo `docker-compose.yml` define o serviço `task-analyzer`, que constrói a imagem a partir do `Dockerfile` e executa o comportamento configurado para o contêiner.

### 1. Validar a configuração

```bash
docker compose config
```

Esse comando verifica se o arquivo de configuração pode ser interpretado corretamente pelo Docker Compose.

### 2. Construir a imagem

```bash
docker compose build
```

### 3. Executar os testes

```bash
docker compose up
```

O Docker Compose inicia o contêiner e executa os testes automatizados. O resultado da execução é apresentado no terminal.

Na execução realizada durante o desenvolvimento, os quatro testes foram aprovados e o contêiner foi encerrado com código de saída `0`, indicando sucesso.

### 4. Executar novamente e remover o contêiner ao finalizar

```bash
docker compose run --rm task-analyzer
```

Esse comando executa o serviço `task-analyzer` e remove o contêiner criado ao término da execução.

## ⚙️ Integração contínua (CI)

O projeto utiliza **GitHub Actions** para automatizar a execução dos testes.

O workflow está localizado em:

```text
.github/workflows/ci.yml
```

### Etapas do workflow

O arquivo de integração contínua configura as seguintes etapas:

1. Baixar o código do repositório.
2. Configurar o Python 3.11.
3. Atualizar o pip.
4. Instalar as dependências definidas em `requirements.txt`.
5. Executar os testes automatizados com pytest.

O workflow está configurado para ser acionado nos eventos definidos no próprio arquivo, incluindo atualizações do repositório, solicitações de pull request e execução manual.

### Como verificar o resultado

Para consultar as execuções:

1. Acesse o repositório no GitHub.
2. Abra a aba **Actions**.
3. Selecione a execução desejada.
4. Confira o resultado das etapas.

Uma execução concluída com sucesso indica que as etapas configuradas no workflow foram finalizadas sem erros.

A integração contínua contribui para identificar falhas antecipadamente e verificar o comportamento do projeto após alterações no código.

## 📐 Especificação e regras de contexto

O projeto segue uma abordagem orientada à especificação, utilizando documentação, regras de contexto e testes automatizados como referências para a implementação.

Os principais arquivos são:

- **`specs/task_analyzer_spec.md`:** especificação do sistema e descrição do comportamento esperado.
- **`CONTEXT_RULES.md`:** regras de contexto consideradas durante o desenvolvimento.
- **`tests/test_harness.py`:** testes automatizados que verificam diferentes cenários de execução.
- **`src/task_analyzer.py`:** implementação do analisador de tarefas.

A utilização desses arquivos ajuda a manter a implementação alinhada ao comportamento especificado e permite validar os resultados por meio de testes reproduzíveis.

## 🎓 Objetivo acadêmico

O projeto foi desenvolvido como parte do **Bootcamp III — Análise e Desenvolvimento de Sistemas (CEUB)**, com foco na aplicação prática de conceitos de especificação de software, implementação, testes automatizados, conteinerização e integração contínua.

O repositório reúne o código-fonte, a especificação, as regras de contexto, os testes e os arquivos de configuração utilizados para executar e validar o sistema.

## 👨‍💻 Autor

**Lucas Frigato**

Projeto acadêmico desenvolvido para o Bootcamp III — Análise e Desenvolvimento de Sistemas (CEUB).
