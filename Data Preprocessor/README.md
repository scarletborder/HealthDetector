# Data Preprocessor
## 使用方法
`python test_dataPreProcessor.py`即可生成一轮新的原始数据并经过预处理得到边数据，同时得到反馈。
```
共生成4755条边数据
前10条为[('Uonwl Rrwdxxxm', 'Lqyhqfzuq Lufwxtbo'), ('Pavbivrq Tkwaiokg', 'Bjduhjek Zrrbae'), ('Pavbivrq Tkwaiokg', 'Nyaqsg Mimzhaot'), ('Xufrp Lylavjf', 'Hgplvzc Yfavhpvm'), ('Xufrp Lylavjf', 'Uqaabplnz Fyvwg'), ('Yyotzdxu Ztgltbhud', 'Kiudne Wydmzftd'), ('Bjduhjek Zrrbae', 'Nyaqsg Mimzhaot'), ('Onombtn Vlahbd', 'Mcenuuh Tstogat'), ('Gvnbgwurk Dnmpmk', 'Tuqmxwxa Emetb'), ('Gvnbgwurk Dnmpmk', 'Rdcoaqgez Wvlzafjt')]
```
生成数据并预处理过程在AMD 5600H Windows x86_64 Python 3.11.6环境下约为11s

## OriginalGenerator
生成原始的数据，模拟现实情况中收集的原始数据。
### 生成格式
本次实验中，将模拟现实情况下两种情况的日志。  
1. 公共交通使用(支付费用)的数据  
    Type: **Transport**
    Example:  
```json
{"Name":"Scarlet","Time":"2024/01/12 19:04:30","Service":"Subway Line2","Detail":{"Method":"AliPay","Discount":0.9}}
```  
> 表示姓名为Scarlet的市民,于2024年1月12日于19时4分30秒乘坐了地铁2号线。（次要信息：使用支付宝支付并享受9折优惠） 

> 在20min内如果两位市民在同一个交通方式内将被视为接触。

2. 饭馆消费情况
    Type: **Shopping**
    Example:
```json
{"Name":"Border","Time":"2023/06/03 21:10:20", "UUID":"f45dbaf8-791a-4397-9807-94a1830b902e", "Detail":{"ShopAddress":"白玉楼","Location":"40.24E 69.23N","Money":"RMB198"}}
```
> 表示姓名为Border的市民，与2023年6月3日于21时10分20秒在白玉楼(uuid:f45dbaf8-791a-4397-9807-94a1830b902e)进行了消费。

> 在1h内如果两位市民在同一个地点消费将被视为接触。

## DataCleaner
清理原始数据，得到可以被后续模块识别的数据。
虽然原始数据不同，但是经过数据所归属的类的逻辑处理后都将得到edges数据。
```python
[("Border","Epicmo"),("Scarlet","Liaosunny123")]
```
表示在任意领域，市民Border和Epicmo有过接触，市民Scarlet和Liaosunny123有过接触。    