# SDD Task Analyzer

Módulo de análise de métricas e produtividade desenvolvido como parte do **Bootcamp III — Análise e Desenvolvimento de Sistemas (CEUB)**.

O projeto utiliza a abordagem **Specification-Driven Development (SDD)**, na qual a especificação e os requisitos orientam o desenvolvimento, a implementação e a validação do software.

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

O projeto também utiliza Docker para executar os testes em um ambiente isolado e GitHub Actions para automatizar sua validação a cada atualização do repositório.

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
| `.github/workflows/ci.yml` | Configuração do fluxo de integração contínua do GitHub Actions. |
| `specs/task_analyzer_spec.md` | Especificação do sistema e comportamento esperado. |
| `src/task_analyzer.py` | Implementação do analisador de tarefas. |
| `tests/test_harness.py` | Testes automatizados para validar o comportamento do sistema. |
| `CONTEXT_RULES.md` | Regras de contexto que orientam o desenvolvimento. |
| `Dockerfile` | Instruções para construir a imagem Docker do projeto. |
| `docker-compose.yml` | Configuração para executar o serviço por meio do Docker Compose. |
| `requirements.txt` | Dependências Python do projeto. |
| `.gitignore` | Arquivos e diretórios que não devem ser versionados. |

## 🛠️ Tecnologias utilizadas

- **Python 3.11:** linguagem utilizada no desenvolvimento.
- **pytest:** framework de testes automatizados.
- **Docker:** ferramenta para empacotar e executar o projeto em um ambiente isolado.
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

Não é necessário instalar as dependências Python diretamente no computador quando a execução é feita utilizando uma imagem Docker que já as instala durante a construção.

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

Os testes do projeto estão localizados em `tests/test_harness.py`.

Para executar a suíte de testes localmente, utilize:

```bash
python -m pytest -v
```

Os testes verificam diferentes cenários de utilização do analisador, incluindo:

- Processamento de dados válidos e cálculo de métricas.
- Tratamento de dados inconsistentes.
- Tratamento de listas vazias.
- Análise de tarefas pendentes.

A execução realizada durante o desenvolvimento apresentou **4 testes aprovados**.

Exemplo de resultado:

```text
4 passed
```

Esse resultado corresponde à execução registrada durante o desenvolvimento. Caso a implementação ou os testes sejam modificados, o resultado poderá ser diferente.

## 🐳 Execução com Docker

O Docker permite construir uma imagem do projeto com suas dependências e executar os testes em um ambiente isolado.

### 1. Construir a imagem

Na raiz do repositório, execute:

```bash
docker build -t sdd-task-analyzer .
```

### 2. Executar os testes

```bash
docker run --rm sdd-task-analyzer
```

O comando executa a instrução definida no `Dockerfile`. Na configuração utilizada durante o desenvolvimento, o contêiner executa os testes automatizados do projeto.

## 🐳 Docker Compose

O arquivo `docker-compose.yml` contém a configuração necessária para executar o serviço do projeto utilizando Docker Compose.

### 1. Validar a configuração

```bash
docker compose config
```

Esse comando verifica se o arquivo de configuração pode ser interpretado corretamente pelo Docker Compose.

### 2. Construir a imagem

```bash
docker compose build
```

### 3. Executar o serviço

```bash
docker compose up
```

O serviço configurado executa os testes automatizados. Após a conclusão, o terminal apresenta o resultado da execução.

Na execução realizada durante o desenvolvimento, o Docker Compose apresentou **4 testes aprovados**, e o contêiner foi encerrado com código de saída `0`, indicando sucesso.

Para executar o serviço em primeiro plano e remover o contêiner ao final, caso o nome do serviço seja `task-analyzer`, também é possível utilizar:

```bash
docker compose run --rm task-analyzer
```

**Observação:** o nome utilizado no último comando precisa corresponder ao nome do serviço definido em `docker-compose.yml`.

## ⚙️ Integração contínua (CI)

O projeto utiliza **GitHub Actions** para automatizar a execução dos testes.

O workflow está localizado em:

```text
.github/workflows/ci.yml
```

O fluxo foi configurado para executar a validação do projeto nos eventos definidos no próprio arquivo, incluindo atualizações da branch principal, solicitações de pull request e execução manual.

### Etapas do workflow

O fluxo de integração contínua contempla as seguintes etapas:

1. Baixar o código do repositório.
2. Configurar o ambiente Python 3.11.
3. Instalar as dependências do projeto.
4. Executar os testes automatizados utilizando pytest.

### Como verificar o resultado

Para consultar as execuções do workflow:

1. Acesse o repositório no GitHub.
2. Abra a aba **Actions**.
3. Selecione uma execução do workflow.
4. Consulte o resultado das etapas.

Uma execução concluída com sucesso indica que as etapas configuradas no workflow foram finalizadas sem erros.

O workflow contribui para a identificação antecipada de falhas e para a manutenção da qualidade do código durante o desenvolvimento.

## 📐 Especificação e regras de contexto

O projeto segue uma abordagem orientada à especificação, utilizando documentação e testes como referências para a implementação.

Os principais arquivos relacionados a esse processo são:

- **`specs/task_analyzer_spec.md`:** documenta a especificação do sistema e o comportamento esperado.
- **`CONTEXT_RULES.md`:** reúne as regras de contexto que devem ser consideradas durante o desenvolvimento.
- **`tests/test_harness.py`:** verifica o comportamento da implementação por meio de cenários automatizados.

A utilização desses arquivos ajuda a manter a implementação alinhada aos requisitos definidos e permite validar o comportamento esperado por meio de testes reproduzíveis.

## 🎓 Objetivo acadêmico

Este projeto foi desenvolvido como parte do **Bootcamp III — Análise e Desenvolvimento de Sistemas (CEUB)**, com foco na aplicação prática de conceitos de especificação de software, implementação, testes automatizados, conteinerização e integração contínua.

O repositório reúne o código-fonte, a especificação, as regras de contexto, os testes e os arquivos de configuração utilizados para executar e validar o sistema.

## 👨‍💻 Autor

**Lucas Frigato**

Projeto acadêmico desenvolvido para o Bootcamp III — Análise e Desenvolvimento de Sistemas (CEUB).
