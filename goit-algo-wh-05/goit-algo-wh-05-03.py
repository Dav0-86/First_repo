import sys 
import datetime 

def parse_log_line(line: str) -> dict:
    parts = line.split()
    date = parts[0]
    time = parts[1]
    date_time = date + " " + time
    date_time = datetime.datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S")

    level = parts[2]
    message = " ".join(parts[3:])
    log = {
        "date_time": date_time,
        "level": level,
        "message": message
    }

    return log


def load_logs(file_path: str) -> list:
    logs = []
    with open(file_path, "r") as file:
        logs = map(parse_log_line, file)
        logs = list(logs)

    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    filtered_logs = filter(lambda log: log["level"] == level, logs)
    filtered_logs = list(filtered_logs)

    return filtered_logs


def count_logs_by_level(logs: list) -> dict:
    counts = {}
    for log in logs:
        level = log["level"]
        if level in counts:
            counts[level] += 1
        else:
            counts[level] = 1

    return counts


def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count}")


def display_log_details(logs, level):
    print(f"\nДеталі логів для рівня '{level}':")
    for log in logs:
        if log["level"] == level:
            print(f"{log['date_time']} - {log['message']}")


args = sys.argv
if len(args) > 1:
    file_path = args[1]
    try:
        logs = load_logs(file_path)
    except IOError as error:
        print(f"Не вдалося прочитати файл: {error}")
        sys.exit(1)
    except Exception as error:
        print(f"Виникла невідома помилка: {error}")
        sys.exit(1)
    else:
        display_log_counts(count_logs_by_level(logs))
if len(args) > 2:
        level = args[2]
        if level in ["INFO", "ERROR", "DEBUG", "WARNING"]:
            display_log_details(logs, level)
        else:
            print(f"Неправильний рівень логування: {level}. Допустимі рівні: INFO, ERROR, DEBUG, WARNING.")
