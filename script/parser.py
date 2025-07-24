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
        help="Путь к JSON-файлу с логами",
    )
    return parser.parse_args()
