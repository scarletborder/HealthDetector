import pickle
import os

from OriginalGenerator import NameGene, Shopping, Transport
import DataCleaner

with open(os.getcwd() + "/Data/edges.pkl", "rb") as fin:
    List = pickle.load(fin)
    print("=" * 30)
    print(f"共生成{len(List)}条边数据\n前10条为{List[:10]}")
