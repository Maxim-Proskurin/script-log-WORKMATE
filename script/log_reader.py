import json
from typing import Any, Dict, List


def read_logs(filepath: str) -> List[Dict[str, Any]]:
    """
    Читает логи из JSON-файла.

    Args:
        filepath (str): Путь к JSON-файлу(ам).

    Returns:
        List[Dict[str, Any]]: Список логов (каждый лог словарь).
    """
    logs = []
    with open(file=filepath, mode="r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                logs.append(json.loads(line))
    return logs
