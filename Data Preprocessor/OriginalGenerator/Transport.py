import pickle
import os
import random
import json
from datetime import datetime, timedelta

DataPath = os.getcwd() + "\\Data"
with open(DataPath + "/NameSet", "rb") as fin:
    NameSet = pickle.load(fin)

NameSet = list(NameSet)
# print(NameSet)
"""
生成交通日志，调控在一个比较密集的并且阳间时间段
"""


# Function to generate random names with 1 to 5 characters
def random_name():
    return random.choice(NameSet)


# Function to generate a random time between two given times
def random_time(start_time, end_time):
    random_time = start_time + timedelta(
        seconds=random.randint(0, int((end_time - start_time).total_seconds()))
    )
    return random_time.strftime("%Y/%m/%d %H:%M:%S")


# Function to generate random service tags
def random_service():
    return f"Subway Line{random.randint(1, 20)}"


# Function to generate random payment methods
def random_method():
    return random.choice(["Alipay", "Wechat", "Visa"])


# Function to generate a random discount
def random_discount():
    return round(random.uniform(0.1, 0.9), 1)


# Function to generate a list of virtual shuttle buses
def generate_virtual_buses(num_buses=20):
    buses = []
    start_date = datetime(2023, 2, 1)
    end_date = datetime(2023, 2, 28)
    start_time = datetime.strptime("06:00:00", "%H:%M:%S").time()
    end_time = datetime.strptime("21:00:00", "%H:%M:%S").time()

    for _ in range(num_buses):
        random_date = start_date + timedelta(
            days=random.randint(0, (end_date - start_date).days)
        )
        time = random_time(
            datetime.combine(random_date, start_time),
            datetime.combine(random_date, end_time),
        )
        service = random_service()
        method = random_method()
        discount = random_discount()
        buses.append(
            {
                "Name": random_name(),
                "Time": time,
                "Service": service,
                "Detail": {"Method": method, "Discount": discount},
            }
        )
    return buses


# Generate the list of 20 virtual shuttle buses
virtual_buses = generate_virtual_buses(4000)
with open(DataPath + "/transport-logs.txt", "w", encoding="utf-8") as fout:
    json.dump(virtual_buses, fout)
