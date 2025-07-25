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
            "Метод generate() должен быть реализован в подклассе.",
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
            headers=[
                "№",
                "handler",
                "total",
                "avg_response_time",
            ],
            tablefmt="grid",
            showindex=False,
            stralign="left",
            numalign="right",
            disable_numparse=True,
        )


class UserAgentReport(Report):
    """
    Отчет по User-Agent.
    """

    def generate(self):
        """
        Группирует логи по user-agent, считает количество для каждого user-agent.
        """
        ua_counts = {}
        for log in self.logs:
            ua = log.get("http_user_agent")
            if ua:
                if ua in ua_counts:
                    ua_counts[ua] += 1
                else:
                    ua_counts[ua] = 1

        # Сортировка по убыванию количества
        sorted_ua = sorted(ua_counts.items(), key=lambda x: x[1], reverse=True)
        table = []
        for i, (ua, count) in enumerate(sorted_ua):
            table.append([i, ua, count])

        return tabulate(
            table,
            headers=["№", "User-Agent", "Count"],
            tablefmt="grid",
            showindex=False,
            stralign="left",
            numalign="right",
            disable_numparse=True,
        )
