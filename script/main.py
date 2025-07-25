from parser import parser_args

from log_reader import read_logs
from report import AverageResponseReport, UserAgentReport


def main():
    """
    Основная CLI-функция: парсит аргументы, читает логи, генерирует и выводит отчет.
    """
    args = parser_args()

    all_logs = []
    for filepath in args.logfile:
        all_logs.extend(read_logs(filepath))

    if args.report == "average":
        report = AverageResponseReport(all_logs)
        print(report.generate())
    elif args.report == "useragent":
        report = UserAgentReport(all_logs)
        print(report.generate())
    else:
        raise ValueError("Unknown report type")


if __name__ == "__main__":
    main()
