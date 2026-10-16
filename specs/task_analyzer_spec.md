# Especificação SDD - Módulo TaskAnalyzer

**Estudante:** Lucas Frigato  
**Curso:** Análise e Desenvolvimento de Sistemas  
**Polo / Turma:** Asa Norte / Bootcamp III  
**Versão:** 1.0  

## Contrato de Interface

### Entradas (Inputs)
Cada tarefa no dataset de entrada contém:
- `id` (str | int): Identificador único da tarefa. Obrigatório.
- `titulo` (str): Descrição/nome da tarefa. Obrigatório.
- `prioridade` (str): Nível de urgência. Valores autorizados: `"Baixa"`, `"Media"`, `"Alta"`.
- `data_criacao` (datetime | str ISO-8601): Data/hora de criação. Obrigatório.
- `data_conclusao` (datetime | str ISO-8601 | None): Data/hora de conclusão. Opcional/Nulo se pendente.
- `status` (str): Estado atual. Valores autorizados: `"Pendente"`, `"Concluida"`, `"Cancelada"`.
- `data_limite` (datetime | str ISO-8601 | None): Data prazo estipulada para conclusão (opcional).

### Saídas (Outputs)
O dicionário retornado possui as seguintes chaves:
- `tempo_medio_conclusao_geral` (float): Média de tempo em horas entre criação e conclusão para tarefas concluídas.
- `tempo_medio_por_prioridade` (dict[str, float]): Média de tempo em horas segmentada por prioridade (`"Baixa"`, `"Media"`, `"Alta"`).
- `taxa_atraso_geral` (float): Percentual (0.0 a 100.0) de tarefas concluídas com atraso em relação ao total de concluídas.
- `taxa_atraso_por_prioridade` (dict[str, float]): Taxa de atraso isolada por prioridade.
- `total_tarefas_analisadas` (int): Contagem total de itens processados no conjunto.
- `indicadores_por_prioridade` (dict[str, dict[str, int]]): Quantidade de tarefas agrupadas por prioridade e status.

### Regras de Negócio
1. **Filtro de Conclusão**: O cálculo de tempo médio e taxa de atraso considera apenas tarefas com `status == "Concluida"` e `data_conclusao` válida.
2. **Consistência Cronológica**: `data_conclusao` nunca pode ser anterior a `data_criacao`. Disparar `TaskValidationError`.
3. **Prevenção de Divisão por Zero**: Conjuntos sem tarefas concluídas retornam médias e taxas zeradas (`0.0`).