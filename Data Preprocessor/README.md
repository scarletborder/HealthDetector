# Data Preprocessor
## 使用方法
`python test_dataPreProcessor.py`即可生成一轮新的原始数据并经过预处理得到边数据，同时得到反馈。
```
共生成4755条边数据
前10条为[('Uonwl Rrwdxxxm', 'Lqyhqfzuq Lufwxtbo'), ('Pavbivrq Tkwaiokg', 'Bjduhjek Zrrbae'), ('Pavbivrq Tkwaiokg', 'Nyaqsg Mimzhaot'), ('Xufrp Lylavjf', 'Hgplvzc Yfavhpvm'), ('Xufrp Lylavjf', 'Uqaabplnz Fyvwg'), ('Yyotzdxu Ztgltbhud', 'Kiudne Wydmzftd'), ('Bjduhjek Zrrbae', 'Nyaqsg Mimzhaot'), ('Onombtn Vlahbd', 'Mcenuuh Tstogat'), ('Gvnbgwurk Dnmpmk', 'Tuqmxwxa Emetb'), ('Gvnbgwurk Dnmpmk', 'Rdcoaqgez Wvlzafjt')]
```
生成数据并预处理过程在AMD 5600H Windows x86_64 Python 3.11.6环境下约为11s

## 注意
由于数据均为随机生成的，所以一些数据在表面看来和现实生活差距较大。例如现实生活中，在早高峰中公共交通会出现高峰，其他时刻则为低谷，并且相同的人群会喜好同一种交通方案（如每天早上都坐同一辆班车上班）。但在模拟数据中，所有时间段的数据平均分布，所有人群都会随机的倾向于任何方案。

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

> 公共交通的基本危险度为8
> 在20min内如果两位市民在同一个交通方式内将被视为接触，同时根据时间的差距和20min的比值来决定最后的危险度。

2. 饭馆消费情况
    Type: **Shopping**
    Example:
```json
{"Name":"Border","Time":"2023/06/03 21:10:20", "UUID":"f45dbaf8-791a-4397-9807-94a1830b902e", "Detail":{"ShopAddress":"白玉楼","Location":"40.24E 69.23N","Money":"RMB198", "Risk":6}}
```
> 表示姓名为Border的市民，与2023年6月3日于21时10分20秒在白玉楼(uuid:f45dbaf8-791a-4397-9807-94a1830b902e)进行了消费。

> 在1h内如果两位市民在同一个地点消费将被视为接触，同时根据时间的差距和1h的比值来决定最后的危险度。

## DataCleaner
清理原始数据，得到可以被后续模块识别的数据。
虽然原始数据不同，但是经过数据所归属的类的逻辑处理后都将得到edges数据。
```python
[("Border","Epicmo","Subway Line4"8),("Scarlet","Liaosunny123","白玉楼",6)]
```
表示市民Border和Epicmo在地铁4号线有过接触，并且危险度为8，市民Scarlet和Liaosunny123在白玉楼有过接触，并且危险度为6。    