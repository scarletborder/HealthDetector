import pickle
import os
import random
import json
from datetime import datetime, timedelta

DataPath: str = os.getcwd() + "\\Data"
with open(DataPath + "/NameSet", "rb") as fin:
    NameSet = pickle.load(fin)

NameSet = list(NameSet)
# print(NameSet)
"""
生成消费日志，调控在一个比较密集的并且阳间时间段
"""
logNumber: int = 5000  # 5000
shops: list = [
    ("cb969aba-90b0-4bbc-ace4-ef6f5b472ca0", "博丽神社", "159.1E 77.58N"),
    ("8434db5d-f466-4ee3-b733-ba092dff69e2", "红魔馆", "-85.58E 40.37N"),
    ("b750fa5a-e0f3-471b-8fef-b2682ce81dbc", "迷途竹林", "-68.65E -86.6N"),
    ("aed6e606-e0cb-43ea-ba6f-7dd7efa47957", "命莲寺", "125.16E 85.51N"),
    ("8b8d70b9-2723-4055-9bb9-b44b7da7913e", "永远亭", "-11.3E 75.97N"),
    ("c47a0d9e-bb6b-4c85-8b7e-ed3186fa3a77", "幻想乡", "-27.35E -39.83N"),
    ("c0d0888c-1de1-4da9-a6db-96f2b2aeba1f", "雾之湖", "14.78E -76.49N"),
    ("135013f4-9a42-4a80-ab81-e5df614f1fb5", "魔法之森", "95.01E -4.75N"),
    ("01f7a701-1539-49b5-ada0-44daaf89888d", "妖怪之山", "13.81E -61.04N"),
    ("b5f34635-fadf-4680-957a-5873a647825d", "白玉楼", "118.81E 55.04N"),
    ("6fe16db5-5452-4195-a334-a73e8aed4fc0", "三途河", "-54.36E 29.41N"),
    ("7f19d135-66a9-421e-ad3e-490a880b9cc8", "地狱", "-3.42E -0.05N"),
    ("1001c561-1d42-47bf-a3c1-e820a9d90809", "冥界", "-174.29E -57.37N"),
    ("9d36f75e-5470-44bf-b884-3aa9364f0fea", "天界", "136.1E 46.34N"),
    ("7ae916b1-de79-4ef3-903b-e5c232439613", "梦幻管", "7.45E -70.82N"),
    ("bbdf6875-d3a4-4a0c-9abc-97ea677bd683", "花映塚", "155.57E 49.83N"),
    ("b1e9f436-8218-46bb-aeed-60e6362e0063", "守矢神社", "154.28E 47.73N"),
    ("1a51f655-c321-475c-8e58-de7c7b116a09", "旧地狱街道", "-74.67E -30.46N"),
    ("b6ba9c38-a24a-4b30-b4bc-34af8531d9f0", "月之都", "-77.53E -68.0N"),
    ("672c595d-c595-4351-bdbf-3364a6154814", "太阳花田", "29.15E 19.63N"),
]


def random_date(start_date, end_date):
    """Return a random datetime between two datetime objects."""
    return start_date + timedelta(
        seconds=random.randint(0, int((end_date - start_date).total_seconds())),
    )


def random_logs(num_logs):
    """Generate a specified number of random logs with corrected time constraints."""
    start_date = datetime(2023, 2, 1)
    end_date = datetime(2023, 2, 28)
    logs = []
    for _ in range(num_logs):
        # Random date
        random_day = random_date(start_date, end_date).date()
        # Random time between 06:00:00 and 21:00:00
        random_hour = random.randint(6, 20)
        random_minute = random.randint(0, 59)
        random_second = random.randint(0, 59)
        random_time = datetime(
            random_day.year,
            random_day.month,
            random_day.day,
            random_hour,
            random_minute,
            random_second,
        )

        name = random.choice(NameSet)
        time = random_time.strftime("%Y/%m/%d %H:%M:%S")
        service = random.choice(shops)
        log = {
            "Name": name,
            "Time": time,
            "UUID": service[0],
            "Detail": {
                "ShopAddress": service[1],
                "Location": service[2],
                "Money": random.randint(50, 500),
            },
        }
        logs.append(log)
    return logs


# Generate 5000 random logs
logs = random_logs(logNumber)
with open(DataPath + "/shopping-logs.txt", "w", encoding="utf-8") as fout:
    json.dump(logs, fout)
