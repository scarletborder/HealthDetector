# 应用层
## 启动方法
```bash
$/HealthDetector/Application> uvicorn networkApi:app --reload
```

## api接口
目前开放以下api
1. **获取社区信息**

   - **URL:** `/get_community_info`
   - **方法:** `GET`
   - **描述:** 返回当前网络图中的社区信息。
   - **响应:** 
     - `200 OK` 成功响应包含社区索引和节点。
     - 示例: 
      ```json
      {
        "CommunityInfo": {
          "0": [
            "Wumbjmam Hfqod",
            "Jwtswowu Zoljc"
          ],
          "1": [
            "Teiwqib Obwdp"
          ],
          "2": [
            "Dsymhmlh Duedvrzak",
            "Sjsrouco Xnlvgb"
          ]
        }
      }
      ```

2. **获取风险地址**

   - **URL:** `/get_riskful_addr`
   - **方法:** `GET`
   - **描述:** 返回当前网络图中标识为风险的地址。
   - **响应:** 
     - `200 OK` 成功响应包含风险地址列表。
     - 示例: 
       ```json
       {
         "riskful": "地狱"
       }
       ```

3. **初始化图**

   - **URL:** `/init_graph/`
   - **方法:** `POST`
   - **描述:** 使用指定的路径初始化网络图。
   - **请求体:** `InitItem` （包含 `loadPath`）
   - **响应:** 
     - `200 OK` 初始化成功。
     - `500 Internal Server Error` 初始化失败。
     - 示例: 
       ```json
       {
         "msg": "success"
       }
       ```

4. **插入边**

   - **URL:** `/insert_edge/`
   - **方法:** `POST`
   - **描述:** 在网络图中插入一条新的边。
   - **请求体:** `NewEdge` （包含 `name1`, `name2`, `service`, `weight`）
    
    | arg     | 类型  | 描述             | 必须 |
    | ------- | ----- | ---------------- | ---- |
    | name1   | str   | 节点1            | 是   |
    | name1   | str   | 节点2            | 是   |
    | service | str   | 交际方式         | 是   |
    | weight  | float | 此交际方式的权重 | 是   |

   - **响应:** 
     - `200 OK` 插入成功。
     - `500 Internal Server Error` 插入失败。
     - 示例: 
       ```json
       {
         "msg": "success"
       }
       ```

---

#### 模型定义

1. **InitItem**
   - `loadPath`: `str | None` — 图的加载路径。

2. **NewEdge**
   - `name1`: `str` — 边的起始节点名称。
   - `name2`: `str` — 边的终止节点名称。
   - `service`: `str` — 边代表的服务类型。
   - `weight`: `float` — 边的权重。

---