import pickle
import os
from OriginalGenerator import NameGene, Shopping, Transport
import DataCleaner

with open(os.getcwd() + "/Data/edges.pkl", "rb") as fin:
    shoppingList = pickle.load(fin)
    print("=" * 30)
    print(f"共生成{len(shoppingList)}条边数据\n前10条为{shoppingList[:10]}")
