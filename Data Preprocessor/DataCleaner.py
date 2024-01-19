import json
import os
import pickle
from datetime import datetime

# name1, name2, addr, weight
edges: list[tuple[str, str, str, float]] = list()


def istimedelta_true(
    t1: str, t2: str, hour: int, min: int, second: int = 0, basicWeight: float = 5.0
) -> float:
    """根据时间间隔返回浮点数权重
    - t1: 格式为2001/02/03 13:04:05
    - hour,min,second: 最大时间间隔
    """
    time1 = datetime.strptime(t1, "%Y/%m/%d %H:%M:%S")
    time2 = datetime.strptime(t2, "%Y/%m/%d %H:%M:%S")

    # 计算时间差
    time_diff = abs(time2 - time1)
    return max(
        0,
        (1 - (time_diff.total_seconds() / (hour * 3600 + min * 60 + second)))
        * basicWeight,
    )


"""
transport
"""

with open(os.getcwd() + "\\Data\\transport-logs.txt", "r", encoding="utf-8") as fin:
    shoppingList: list[dict] = json.load(fin)

# service:[(name,time),]
appear: dict[str, list[tuple[str, str]]] = dict()
for item in shoppingList:
    ii = appear.get(item["Service"], list())
    ii.append((item["Name"], item["Time"]))
    appear[item["Service"]] = ii

# print(appear)
for key, addrList in appear.items():
    if len(addrList) < 2:
        continue
    for p1 in range(0, len(addrList) - 1):
        for p2 in range(p1 + 1, len(addrList)):
            weight = istimedelta_true(addrList[p1][1], addrList[p2][1], 1, 0, 0, 8)
            if weight > 0:  # 交通方式默认8risk
                edges.append((addrList[p1][0], addrList[p2][0], key, weight))


"""
shopping
"""
with open(os.getcwd() + "\\Data\\shopping-logs.txt", "r", encoding="utf-8") as fin:
    shoppingList: list[dict] = json.load(fin)

# uuid:[(name,time),]
appear: dict[str, list[tuple[str, str]]] = dict()
for item in shoppingList:
    ii = appear.get(
        item["UUID"]
        + " "
        + str(item["Detail"]["Risk"])
        + " "
        + item["Detail"]["ShopAddress"],
        list(),
    )
    ii.append((item["Name"], item["Time"]))
    appear[
        item["UUID"]
        + " "
        + str(item["Detail"]["Risk"])
        + " "
        + item["Detail"]["ShopAddress"]
    ] = ii

# print(appear)
for key, addrList in appear.items():
    if len(addrList) < 2:
        continue
    key = key.rsplit(" ")
    addr = key[-1]
    basicRisk = float(key[-2])
    for p1 in range(0, len(addrList) - 1):
        for p2 in range(p1 + 1, len(addrList)):
            weight = istimedelta_true(
                addrList[p1][1], addrList[p2][1], 1, 0, 0, basicWeight=basicRisk
            )
            if weight > 0:
                edges.append((addrList[p1][0], addrList[p2][0], addr, weight))


"""
保存
"""
with open(os.getcwd() + "\\Data\\edges.pkl", "wb") as fout:
    pickle.dump(edges, fout)
