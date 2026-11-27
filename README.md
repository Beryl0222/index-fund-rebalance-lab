# 指数换仓前后的可交易头寸与净值归因

提供指数公告、证券生命周期、行情和买卖回报，用于离线重放现券组合的换仓日。

在仓库根目录使用 Python 3.11 的标准库。资料用 UTF-8 CSV 保存，空字段的含义见数据说明。

```sh
python3 inspect_inputs.py
python3 -m unittest discover -s tests -v
```

查看入口按表列出记录数及原始字段。资料测试核对文件接口和关键跨表引用。业务时点、计量单位及来源字段见[数据说明](data/README.md)。
