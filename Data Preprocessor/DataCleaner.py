import json
import os
import pickle
from datetime import datetime

edges: list[tuple[str, str]] = list()


def istimedelta_true(t1: str, t2: str, hour: int, min: int, second: int = 0) -> bool:
    """判断时间间隔是否小于预设值
    - t1: 格式为2001/02/03 13:04:05
    """
    time1 = datetime.strptime(t1, "%Y/%m/%d %H:%M:%S")
    time2 = datetime.strptime(t2, "%Y/%m/%d %H:%M:%S")

    # 计算时间差
    time_diff = abs(time2 - time1)
    return time_diff.total_seconds() < hour * 3600 + min * 60 + second


"""
transport
"""

with open(os.getcwd() + "\\Data\\transport-logs.txt", "r", encoding="utf-8") as fin:
    shoppingList: list[dict] = json.load(fin)

# uuid:[(name,time),]
appear: dict[str, list[tuple[str, str]]] = dict()
for item in shoppingList:
    ii = appear.get(item["Service"], list())
    ii.append((item["Name"], item["Time"]))
    appear[item["Service"]] = ii

# print(appear)
for addrList in appear.values():
    if len(addrList) < 2:
        continue
    for p1 in range(0, len(addrList) - 1):
        for p2 in range(p1 + 1, len(addrList)):
            if istimedelta_true(addrList[p1][1], addrList[p2][1], 1, 0) is True:
                edges.append((addrList[p1][0], addrList[p2][0]))


"""
shopping
"""
with open(os.getcwd() + "\\Data\\shopping-logs.txt", "r", encoding="utf-8") as fin:
    shoppingList: list[dict] = json.load(fin)

# uuid:[(name,time),]
appear: dict[str, list[tuple[str, str]]] = dict()
for item in shoppingList:
    ii = appear.get(item["UUID"], list())
    ii.append((item["Name"], item["Time"]))
    appear[item["UUID"]] = ii

# print(appear)
for addrList in appear.values():
    if len(addrList) < 2:
        continue
    for p1 in range(0, len(addrList) - 1):
        for p2 in range(p1 + 1, len(addrList)):
            if istimedelta_true(addrList[p1][1], addrList[p2][1], 1, 0) is True:
                edges.append((addrList[p1][0], addrList[p2][0]))


"""
保存
"""
with open(os.getcwd() + "\\Data\\edges.pkl", "wb") as fout:
    pickle.dump(edges, fout)
