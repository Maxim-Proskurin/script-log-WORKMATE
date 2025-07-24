from typing import Any, Dict, List

from tabulate import tabulate


class Report:
    """
    Базовый класс для всех отчетов.
    """

    def __init__(self, logs: List[Dict[str, Any]]) -> None:
        self.logs = logs

        def generate(self) -> str:
            """
            Генерирует отчет.
            Retutns:
                str: Отчет в виде строки(например таблица).
            """
            raise NotImplementedError(
                "Метод generate() должен быть реализован в подклассе."
            )


class AverageResponseReport(Report):
    """
    Отчет по среднему времени ответа с группировкой по URL.
    """

    def generate(self) -> str:
        """
        Группирует логи по url,
        считает количество и среднее время ответа для каждого url.
        """
        url_stats = {}
        for log in self.logs:
            url = log.get("url", "Неизвестно")
            if "response_time" in log:
                if url not in url_stats:
                    url_stats[url] = []
                url_stats[url].append(log["response_time"])

        # Сортировка по количеству (от большего к меньшему)
        sorted_stats = sorted(
            url_stats.items(), key=lambda item: len(item[1]), reverse=True
        )
        table = []
        for i, (url, times) in enumerate(sorted_stats):
            count = len(times)
            avg = sum(times) / count if count else 0
            avg = round(avg, 3)
            table.append([i, url, count, avg])

        return tabulate(
            table,
            headers=["№", "handler", "total", "avg_response_time"],
            tablefmt="github",
        )


class UserAgentReport(Report):
    """
    Отчет по User-Agent.
    """

    def generate(self) -> str:
        agents = set(
            log["http_user_agent"] for log in self.logs if "http_user_agent" in log
        )
        table = [[agent] for agent in agents]
        return tabulate(table, headers=["User-Agent"], tablefmt="github")
