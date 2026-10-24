# SDD Task Analyzer

Módulo de análise de métricas e produtividade desenvolvido como parte do **Bootcamp III — Análise e Desenvolvimento de Sistemas (CEUB)**.

O projeto tem como objetivo analisar listas de tarefas e gerar métricas de produtividade a partir de seus dados, seguindo as regras e os requisitos definidos na documentação de Software Design Description (SDD).

## 📋 Sumário

- [Visão geral](#-visão-geral)
- [Estrutura do projeto](#-estrutura-do-projeto)
- [Requisitos](#-requisitos)
- [Tecnologias utilizadas](#-tecnologias-utilizadas)
- [Execução local](#-execução-local)
- [Execução dos testes](#-execução-dos-testes)
- [Execução com Docker](#-execução-com-docker)
- [Integração contínua (CI)](#-integração-contínua-ci)
- [Regras de contexto](#-regras-de-contexto)
- [Documentação](#-documentação)

## 🎯 Visão geral

O Task Analyzer é um módulo Python que recebe dados de tarefas, processa as informações de acordo com as regras definidas no projeto e retorna métricas relacionadas à produtividade.

O desenvolvimento segue uma abordagem orientada à especificação (Specification-Driven Development — SDD), utilizando documentação de requisitos, regras de contexto e testes automatizados para orientar e validar a implementação.

## 📁 Estrutura do projeto

```text
sdd-task-analyzer/
├── .github/
│   └── workflows/
│       └── ci.yml
├── specs/
│   ├── system_design_document.pdf
│   └── requirements.yaml
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

**Observação:** os nomes e arquivos dentro de `specs/`, `src/` e `tests/` devem corresponder aos arquivos efetivamente presentes no repositório.

## 📌 Requisitos

Para executar o projeto localmente, são necessários:

- Python 3.11 ou superior.
- pip para instalação das dependências.

Para executar com contêineres:

- Docker Desktop ou outra instalação compatível com Docker Engine.
- Docker Compose.

Para utilizar a integração contínua, é necessário que o repositório esteja hospedado no GitHub com o workflow configurado em `.github/workflows/ci.yml`.

## 🛠️ Tecnologias utilizadas

- **Python 3.11:** linguagem utilizada na implementação.
- **pytest:** execução dos testes automatizados.
- **Docker:** criação de um ambiente isolado para executar o projeto e os testes.
- **Docker Compose:** configuração e execução do serviço em contêiner.
- **GitHub Actions:** automação da execução dos testes a cada atualização do repositório.

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

## 🧪 Execução dos testes

Com as dependências instaladas, execute:

```bash
python -m pytest -v
```

Os testes verificam os cenários definidos no arquivo `tests/test_harness.py`, incluindo os casos de sucesso, inconsistência dos dados, lista vazia e tarefas pendentes, conforme implementados na suíte de testes.

### Resultado esperado

Na execução local realizada durante o desenvolvimento, os quatro testes automatizados passaram.

Exemplo de resultado:

```text
4 passed
```

O resultado pode variar caso os testes ou a implementação sejam modificados.

## 🐳 Execução com Docker

O Docker permite executar os testes em um ambiente isolado, sem precisar instalar as dependências Python diretamente no ambiente do usuário.

### 1. Construir a imagem

Na raiz do repositório, execute:

```bash
docker build -t sdd-task-analyzer .
```

### 2. Executar os testes no contêiner

```bash
docker run --rm sdd-task-analyzer
```

O comando executa o comportamento configurado no `Dockerfile`. Na configuração atual do projeto, a imagem é utilizada para executar os testes automatizados.

## 🐳 Execução com Docker Compose

O arquivo `docker-compose.yml` define a configuração do serviço utilizado para executar o projeto em contêiner.

### 1. Validar a configuração

```bash
docker compose config
```

### 2. Construir a imagem

```bash
docker compose build
```

### 3. Executar o serviço

```bash
docker compose up
```

O serviço executa os testes automatizados definidos no projeto. Quando a execução terminar, o resultado poderá ser consultado no terminal.

Para executar e remover o contêiner ao finalizar:

```bash
docker compose run --rm task-analyzer
```

> **Importante:** o último comando pressupõe que o serviço no arquivo `docker-compose.yml` se chama `task-analyzer`. Caso o nome seja diferente, utilize o nome definido no arquivo.

## ⚙️ Integração contínua (CI)

O projeto utiliza GitHub Actions para automatizar a execução dos testes.

O workflow está localizado em:

```text
.github/workflows/ci.yml
```

O fluxo está configurado para ser acionado em eventos de atualização da branch `main`, solicitações de pull request direcionadas a essa branch e execução manual, conforme definido no arquivo de workflow.

### Etapas do workflow

1. Baixar o código do repositório.
2. Configurar o Python 3.11.
3. Instalar as dependências especificadas em `requirements.txt`.
4. Executar os testes automatizados com `pytest`.

### Verificar a execução

Para consultar os resultados:

1. Abra o repositório no GitHub.
2. Acesse a aba **Actions**.
3. Selecione a execução desejada.
4. Confira se as etapas foram concluídas com sucesso.

A integração contínua ajuda a identificar problemas de implementação antes que alterações sejam incorporadas ao projeto.

## 📐 Regras de contexto

O arquivo `CONTEXT_RULES.md` documenta as regras de contexto utilizadas como referência durante o desenvolvimento.

Essas regras devem ser consideradas junto à documentação de requisitos e à especificação do sistema para manter a implementação alinhada ao comportamento esperado.

As regras de contexto e os requisitos documentados devem orientar tanto a implementação quanto a validação por meio dos testes automatizados.

## 📚 Documentação

A documentação técnica do projeto está organizada no diretório `specs/`.

Ela reúne a especificação do sistema e os requisitos utilizados como base para a implementação, conforme os arquivos presentes no repositório.

Consulte também:

- `CONTEXT_RULES.md` — regras de contexto do projeto.
- `tests/test_harness.py` — testes automatizados.
- `src/task_analyzer.py` — implementação do analisador de tarefas.
- `Dockerfile` — instruções para construção da imagem Docker.
- `docker-compose.yml` — configuração do serviço executado pelo Docker Compose.
- `.github/workflows/ci.yml` — configuração da integração contínua.

## 👨‍💻 Autor

**Lucas Frigato**

Projeto acadêmico desenvolvido para o Bootcamp III — Análise e Desenvolvimento de Sistemas (CEUB).
