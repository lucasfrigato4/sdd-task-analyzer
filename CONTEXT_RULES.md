# Diretrizes e Governança de Contexto (CONTEXT_RULES)

## 1. Diretrizes Arquiteturais (Obrigatórias)
- Utilizar estritamente Python 3.11 ou superior.
- Aplicar obrigatoriamente type hints (anotações de tipo) em todas as funções, métodos, parâmetros e retornos.
- Obedecer rigorosamente ao princípio de responsabilidade única (SRP) e à PEP 8.
- Incluir documentação formal padronizada (Google style docstrings) em todos os módulos, classes e funções.
- Escrever funções pequenas, altamente coesas e focadas em uma única atribuição.
- Implementar tratamento de exceções customizado e específico, acompanhado de mensagens descritivas.
- Utilizar logs estruturados por meio do módulo padrão `logging` em vez de `print()`.

## 2. Proibições Explícitas
- NÃO utilizar bibliotecas externas não autorizadas no `requirements.txt`.
- NÃO alterar, remover ou burlar os cenários de teste definidos no contrato.
- NÃO modificar a estrutura de pastas e arquivos especificada.
- NÃO implementar persistência em arquivos locais (.txt, .json, .csv) ou banco de dados nesta etapa.
- NÃO alterar a assinatura (nome, ordem e tipagem dos parâmetros) das funções públicas estipuladas.
- NÃO gerar código sem os testes automatizados correspondentes no Test Harness.
- NÃO introduzir código duplicado, redundante ou desnecessário ("código morto").
- NÃO assumir regras de negócio implícitas não descritas no contrato SDD.