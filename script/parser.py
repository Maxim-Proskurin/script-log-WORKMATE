import argparse


def parser_args():
    """
    Парсит аргументы командной строки для Лог-репорт.

    Returns:
        argparse.Namespace: Пространство имен с аргументами командной строки.
    """
    parser = argparse.ArgumentParser(description="Лог-репорт")
    parser.add_argument(
        "logfile",
        nargs="+",
        help="Один или несколько путей к JSON-файлам с логами",
    )
    parser.add_argument(
        "--report",
        choices=["average", "useragent"],
        required=True,
        help="Тип отчета (например: average)",
    )

    return parser.parse_args()
