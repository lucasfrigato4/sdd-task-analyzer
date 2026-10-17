"""Módulo responsável pelo processamento de métricas e indicadores de produtividade de tarefas.

Este módulo implementa o contrato de interface SDD definido na Fase 1,
garantindo type hints, logging estruturado, validações cronológicas e
tratamento seguro contra divisão por zero.
"""

from datetime import datetime
import logging
from typing import Any, Dict, List, Optional, Union

# Configuração de logging estruturado
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger("TaskAnalyzer")


class TaskValidationError(Exception):
    """Exceção customizada para erros de validação nas regras de negócio e datas de tarefas."""

    pass


def _parse_datetime(dt_val: Union[datetime, str, None]) -> Optional[datetime]:
    """Converte um valor ISO-8601 ou datetime para um objeto datetime validado.

    Args:
        dt_val: Objeto datetime, string formatada em ISO-8601 ou None.

    Returns:
        Objeto datetime convertido ou None caso a entrada seja nula/vazia.

    Raises:
        TaskValidationError: Se a string não estiver em formato ISO válido.
    """
    if dt_val is None:
        return None
    if isinstance(dt_val, datetime):
        return dt_val
    if isinstance(dt_val, str):
        try:
            return datetime.fromisoformat(dt_val)
        except ValueError as err:
            raise TaskValidationError(f"Formato de data/hora inválido: {dt_val}") from err
    raise TaskValidationError(f"Tipo de dado inesperado para data/hora: {type(dt_val)}")


def analyze_tasks(tasks: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Processa uma lista de tarefas e gera métricas e indicadores consolidados de produtividade.

    Args:
        tasks: Lista de dicionários representando o contrato de entrada das tarefas.

    Returns:
        Dicionário com indicadores consolidados, tempos médios e taxas de atraso.

    Raises:
        TaskValidationError: Se houver inconsistência nas datas (ex: data_conclusao < data_criacao).
    """
    logger.info("Iniciando a análise de %d tarefas.", len(tasks))

    prioridades_validas = ["Baixa", "Media", "Alta"]
    
    # Inicialização das estruturas de apoio
    indicadores_por_prioridade: Dict[str, Dict[str, int]] = {
        p: {"Pendente": 0, "Concluida": 0, "Cancelada": 0} for p in prioridades_validas
    }
    
    tempos_conclusao_por_prioridade: Dict[str, List[float]] = {p: [] for p in prioridades_validas}
    atrasos_por_prioridade: Dict[str, List[bool]] = {p: [] for p in prioridades_validas}

    todas_horas_conclusao: List[float] = []
    todos_atrasos: List[bool] = []

    for task in tasks:
        prio = task.get("prioridade", "Baixa")
        if prio not in prioridades_validas:
            prio = "Baixa"

        status = task.get("status", "Pendente")
        if status in indicadores_por_prioridade[prio]:
            indicadores_por_prioridade[prio][status] += 1

        dt_criacao = _parse_datetime(task.get("data_criacao"))
        dt_conclusao = _parse_datetime(task.get("data_conclusao"))
        dt_limite = _parse_datetime(task.get("data_limite"))

        if status == "Concluida" and dt_conclusao is not None:
            if dt_criacao is None:
                raise TaskValidationError(f"Tarefa {task.get('id')} concluída sem data_criacao válida.")

            # Regra de Consistência Cronológica
            if dt_conclusao < dt_criacao:
                err_msg = (
                    f"Inconsistência na tarefa '{task.get('id')}': "
                    f"data_conclusao ({dt_conclusao}) é anterior à data_criacao ({dt_criacao})."
                )
                logger.error(err_msg)
                raise TaskValidationError(err_msg)

            # Cálculo de tempo gasto em horas
            horas_gastas = (dt_conclusao - dt_criacao).total_seconds() / 3600.0
            todas_horas_conclusao.append(horas_gastas)
            tempos_conclusao_por_prioridade[prio].append(horas_gastas)

            # Cálculo de atraso em relação à data limite esperada
            estava_atrasada = False
            if dt_limite is not None and dt_conclusao > dt_limite:
                estava_atrasada = True
            
            todos_atrasos.append(estava_atrasada)
            atrasos_por_prioridade[prio].append(estava_atrasada)

    # Cálculo seguro de médias e percentuais (Prevenção de Divisão por Zero)
    tempo_medio_conclusao_geral = (
        sum(todas_horas_conclusao) / len(todas_horas_conclusao) if todas_horas_conclusao else 0.0
    )

    taxa_atraso_geral = (
        (sum(1 for a in todos_atrasos if a) / len(todos_atrasos)) * 100.0 if todos_atrasos else 0.0
    )

    tempo_medio_por_prioridade: Dict[str, float] = {}
    taxa_atraso_por_prioridade: Dict[str, float] = {}

    for p in prioridades_validas:
        tempos_p = tempos_conclusao_por_prioridade[p]
        atrasos_p = atrasos_por_prioridade[p]

        tempo_medio_por_prioridade[p] = (
            sum(tempos_p) / len(tempos_p) if tempos_p else 0.0
        )
        taxa_atraso_por_prioridade[p] = (
            (sum(1 for a in atrasos_p if a) / len(atrasos_p)) * 100.0 if atrasos_p else 0.0
        )

    logger.info("Processamento concluído com sucesso.")

    return {
        "tempo_medio_conclusao_geral": round(tempo_medio_conclusao_geral, 2),
        "tempo_medio_por_prioridade": {
            k: round(v, 2) for k, v in tempo_medio_por_prioridade.items()
        },
        "taxa_atraso_geral": round(taxa_atraso_geral, 2),
        "taxa_atraso_por_prioridade": {
            k: round(v, 2) for k, v in taxa_atraso_por_prioridade.items()
        },
        "total_tarefas_analisadas": len(tasks),
        "indicadores_por_prioridade": indicadores_por_prioridade,
    }