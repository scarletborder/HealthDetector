import pickle
import os
from collections import defaultdict
import networkx as nx
import community as community_louvain
import matplotlib.pyplot as plt
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class myNetwork:
    def flush_edges(self):
        """初次导入使用pkl edges文件"""
        # 添加边，模拟社交联系
        with open(os.getcwd() + "/../Data Preprocessor/Data/edges.pkl", "rb") as fin:
            edges = pickle.load(fin)
        for edge in edges:
            self.G.add_edge(edge[0], edge[1], weight=edge[3], location=edge[2])
        self.dirty = True
        pass

    def add_edge(self, e: tuple[str, str, float, str]):
        """后续加边"""
        self.G.add_edge(e[0], e[1], weight=e[3], location=e[2])
        self.dirty = True
        pass

    def update_partition(self):
        # 使用Louvain方法进行社区发现
        self.partition = community_louvain.best_partition(self.G, weight="weight")
        # 识别关键地点
        self.location_risk = defaultdict(float)
        for _, _, data in self.G.edges.data():
            location = data["location"]
            weight = data["weight"]  # 用作风险分数的一部分
            self.location_risk[location] += weight
        self.dirty = False
        pass

    def save_fig(self):
        if self.dirty is True:
            self.update_partition()
        # 绘制网络图和社区
        pos = nx.spring_layout(self.G)
        plt.figure(figsize=(8, 8))
        # 绘制节点
        for community in set(self.partition.values()):
            list_nodes = [
                nodes
                for nodes in self.partition.keys()
                if self.partition[nodes] == community
            ]
            nx.draw_networkx_nodes(
                self.G,
                pos,
                list_nodes,
                node_size=200,
                node_color=str(community / max(self.partition.values())),
            )

        nx.draw_networkx_edges(self.G, pos, alpha=0.5)
        plt.savefig(os.getcwd() + "/pic.jpg")
        plt.show()

    def __init__(self, loadPath: str | None = None) -> None:
        # 创建一个示例网络
        self.dirty: bool = True
        if loadPath is None:
            self.G = nx.Graph()
            # self.partition = None
            self.flush_edges()
        else:
            with open(loadPath, "rb") as fin:
                self.G = pickle.load(fin)

    def save_graph(self, savePath: str):
        with open(savePath, "wb") as fout:
            pickle.dump(self.G, fout)

    def get_community_info(self):
        if self.dirty is True:
            self.update_partition()
        community_list = dict()
        for node, community in self.partition.items():
            cm = community_list.get(community, [])
            cm.append(node)
            community_list[community] = cm

        return community_list

    def get_riskful_addr(self):
        if self.dirty is True:
            self.update_partition()
        # 最大风险地点
        maxNum = -1
        maxIdx = ""
        for idx, nodes in self.location_risk.items():
            # print(f"{idx} is {nodes} risk")
            if nodes > maxNum:
                maxIdx = idx
                maxNum = nodes

        return maxIdx


MyNetWork = myNetwork()

app = FastAPI()


@app.get("/get_community_info")
async def get_community_info():
    com = MyNetWork.get_community_info()
    return {"CommunityInfo": com}


@app.get("/get_riskful_addr")
async def get_riskful_addr():
    return {"riskful": MyNetWork.get_riskful_addr()}


class InitItem(BaseModel):
    loadPath: str | None = None


@app.post("/init_graph/")
async def init_graph(loadPath: InitItem):
    global MyNetWork
    try:
        MyNetWork = myNetwork(loadPath.loadPath)
    except BaseException:
        raise HTTPException(status_code=500, detail="remote error")
    else:
        return {"msg": "success"}


class NewEdge(BaseModel):
    name1: str
    name2: str
    service: str
    weight: float


@app.post("/insert_edge/")
async def insert_edge(newedge: NewEdge):
    global MyNetWork
    try:
        MyNetWork.add_edge(
            (newedge.name1, newedge.name2, newedge.weight, newedge.service)
        )
    except BaseException:
        raise HTTPException(status_code=500, detail="remote error")
    else:
        return {"msg": "success"}
