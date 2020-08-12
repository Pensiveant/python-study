# 爬取一家上市公司的年报并存取到mysql

---

## 数据来源

---

## 数据表设计

### 资产负债表

BalanceSheet（资产负债表）

> **资产**

字段|含义
---|---
cash|货币资金
Inventories|存货
ShortTermInvestments|短期投资
NotesReceviable|应收票据
DividendReceviable|应收股利
InterestReceviable|应收利息
AccountsReceviable|应收账款
OthersReceviables|其他应收款
AccountsPrepaid|预付款项
PrepaidAndDeferredExpenses|待摊费用
OtherCurrentAssets|其他流动资产

> **负债**

字段|含义
---|---
Short-termLoans|短期借款
AccruedPayroll| 应付工资
AccountsPayable| 应付账款
TaxesPayable| 应交税金
OtherCreditors|其他应付款

> **股东权益**

字段|含义
--|--
SubscribedCapital |股本
CapitalSurplus |资本公积
RetainedEarnings|未分配利润
surplusReserve  |盈余公积

### 利润表

Income Statement(利润表)

字段|含义
|营业总收入
|营业总成本
|营业利润
|利润总额
|净利润

字段|含义
--|---
|营业收入
| 

### 现金流量表

Cash Flows Statement(现金流量表)

字段|含义
--|---


---

## 技术路线
