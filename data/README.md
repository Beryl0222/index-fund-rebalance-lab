# 数据说明

所有数据均为合成资料。每张表的首行为字段名。

金额使用人民币，行情为未复权数。组合目标用组合权益乘权重，再按交易单位取能买卖的股数，观察到任何市场状态前不能用该证券新报价。成份有效期从 effective 当日开盘起。实际回报按证券、买卖方向和交易时点认领当日有效指令，超过有效量或不在时段的回报留为待核，禁止自动补造委托。T+1 的可卖日等于资料给出的买入交收日。现金红利使用登记日收盘经济头寸，除权计入应收，付款日成为现金。拆股比例在除权日起适用，拆股在相应报价上只能调整一次。净值本币计量，费用单列，归因需注明计量基点且加总能解释总差异。没有已知报价的头寸须明确缺估值。策略每日以 sessions 的 decision_utc 作为交易决策时点。两次独立回放均以 opening_portfolio 为期初、没有挂单。首日持有的旧基准视为已有目标，新目标生效或可按策略提前采纳时才形成新的换仓意图。证券日历缺少对应日期时，该日没有可用的交易窗口。成交回报所属策略由 strategy 指定，各策略资金、交易量上限和剩余委托相互独立。权威指数收盘点位用于共同收益比较，成份权重用于目标与偏离解释。

## index_notices

- `notice` 版本
- `known` 可见时点 UTC
- `effective` 基准生效日
- `weights` 证券与目标权重

## opening_portfolio

- `asset` 证券或 CASH
- `units` 期初可卖股数或已交收现金

## security_calendar

- `asset` 证券
- `day` 交易日
- `open_utc` 开市 UTC，空表示停牌
- `close_utc` 收市 UTC
- `lot` 最小交易单位
- `max_volume` 该证券策略在本时段可用成交量上限
- `lower` 最低成交价
- `upper` 最高成交价

## corporate_actions

- `action` 权益号
- `asset` 证券
- `kind` split 或 cash_div
- `known` 公告 UTC
- `record` 权益登记日
- `ex_day` 除权日
- `pay_day` 到账日
- `rate` 新旧股比例或每股现金

## quotes

- `id` 报价
- `asset` 证券
- `for_day` 报价日期
- `known` 可见 UTC
- `price` 本币未复权价格
- `revises` 被替换报价

## execution_tape

- `fill` 模拟盘回报号
- `day` 交易日
- `time` UTC
- `asset` 证券
- `side` buy 或 sell
- `shares` 股数
- `price` 成交价格
- `fee` 元
- `settle` 交收日
- `strategy` 对应策略标识

## sessions

- `day` 交易日
- `decision_utc` 产生目标委托的 UTC 时刻
- `nav_utc` 归档净值的 UTC 时刻
- `benchmark_level` 权威指数收盘点位

## strategy_profiles

- `strategy` 策略标识，与模拟成交回报对应
- `target_timing` announced 可在公告后的首个决策时点采用即将生效的目标，effective 只采用已知且已生效的目标
