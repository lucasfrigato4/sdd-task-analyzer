"""Suíte de testes automatizados (Test Harness) utilizando pytest.

Valida integralmente o contrato executável SDD, incluindo os Cenários 1 (Sucesso),
Cenário 2 (Exceção/Inconsistência de Datas) e Casos de Borda (Prevenção de Divisão por Zero).
"""

from datetime import datetime, timedelta
import pytest
from src.task_analyzer import TaskValidationError, analyze_tasks


def test_cenario_1_sucesso_metricas_corretas():
    """Valida o Cenário 1 de Sucesso: cálculo exato de tempos médios, taxas de atraso e agrupamentos."""
    base_time = datetime(2026, 10, 10, 10, 0, 0)

    tasks_dataset = [
        {
            "id": "T001",
            "titulo": "Implementar Login",
            "prioridade": "Alta",
            "data_criacao": base_time.isoformat(),
            "data_limite": (base_time + timedelta(hours=10)).isoformat(),
            "data_conclusao": (base_time + timedelta(hours=5)).isoformat(),
            "status": "Concluida",
        },
        {
            "id": "T002",
            "titulo": "Corrigir Layout",
            "prioridade": "Alta",
            "data_criacao": base_time.isoformat(),
            "data_limite": (base_time + timedelta(hours=5)).isoformat(),
            "data_conclusao": (base_time + timedelta(hours=15)).isoformat(),
            "status": "Concluida",
        },
        {
            "id": "T003",
            "titulo": "Atualizar README",
            "prioridade": "Baixa",
            "data_criacao": base_time.isoformat(),
            "data_limite": (base_time + timedelta(hours=20)).isoformat(),
            "data_conclusao": (base_time + timedelta(hours=10)).isoformat(),
            "status": "Concluida",
        },
        {
            "id": "T004",
            "titulo": "Refatorar Módulo",
            "prioridade": "Media",
            "data_criacao": base_time.isoformat(),
            "data_limite": None,
            "data_conclusao": None,
            "status": "Pendente",
        },
    ]

    result = analyze_tasks(tasks_dataset)

    assert result["total_tarefas_analisadas"] == 4
    # Tempos gastos: T001=5h, T002=15h, T003=10h. Média geral = (5 + 15 + 10) / 3 = 10.0h
    assert result["tempo_medio_conclusao_geral"] == 10.0
    # Prioridade Alta: (5 + 15) / 2 = 10.0h. Baixa: 10.0h. Media: 0.0h
    assert result["tempo_medio_por_prioridade"]["Alta"] == 10.0
    assert result["tempo_medio_por_prioridade"]["Baixa"] == 10.0
    assert result["tempo_medio_por_prioridade"]["Media"] == 0.0

    # Atrasos: T001 (5h <= 10h ok), T002 (15h > 5h atrasada), T003 (10h <= 20h ok).
    # 1 atraso em 3 concluídas = 33.33%
    assert result["taxa_atraso_geral"] == 33.33
    assert result["taxa_atraso_por_prioridade"]["Alta"] == 50.0

    # Indicadores por status e prioridade
    assert result["indicadores_por_prioridade"]["Alta"]["Concluida"] == 2
    assert result["indicadores_por_prioridade"]["Baixa"]["Concluida"] == 1
    assert result["indicadores_por_prioridade"]["Media"]["Pendente"] == 1


def test_cenario_2_excecao_datas_inconsistentes():
    """Valida o Cenário 2: disparo de TaskValidationError quando data_conclusao < data_criacao."""
    base_time = datetime(2026, 10, 10, 10, 0, 0)

    invalid_dataset = [
        {
            "id": "ERR01",
            "titulo": "Tarefa com Viagem no Tempo",
            "prioridade": "Alta",
            "data_criacao": base_time.isoformat(),
            "data_conclusao": (base_time - timedelta(hours=2)).isoformat(),  # Conclusão anterior à criação
            "status": "Concluida",
        }
    ]

    with pytest.raises(TaskValidationError) as exc_info:
        analyze_tasks(invalid_dataset)

    assert "anterior" in str(exc_info.value) or "Inconsistência" in str(exc_info.value)


def test_caso_de_borda_lista_vazia():
    """Valida a prevenção de divisão por zero com entrada vazia."""
    result = analyze_tasks([])

    assert result["total_tarefas_analisadas"] == 0
    assert result["tempo_medio_conclusao_geral"] == 0.0
    assert result["taxa_atraso_geral"] == 0.0
    assert result["tempo_medio_por_prioridade"]["Alta"] == 0.0


def test_caso_de_borda_apenas_pendentes():
    """Valida retorno sem exceção quando não existem tarefas concluídas."""
    tasks_dataset = [
        {
            "id": "P01",
            "titulo": "Pendente 1",
            "prioridade": "Media",
            "data_criacao": datetime.now().isoformat(),
            "data_conclusao": None,
            "status": "Pendente",
        }
    ]

    result = analyze_tasks(tasks_dataset)

    assert result["total_tarefas_analisadas"] == 1
    assert result["tempo_medio_conclusao_geral"] == 0.0
    assert result["taxa_atraso_geral"] == 0.0
    assert result["indicadores_por_prioridade"]["Media"]["Pendente"] == 1