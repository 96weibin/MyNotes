
## features

Userstory | Description | area | comment
-|-|-|-
85846 UI: Diagnostics UI PI2 | 更新solver-log -> dignostic | graphql, toolbar, each panel | 更清晰的显示 run reconcile 的结果
6720 UI: Clarify tolerance and imbalance reporting. | 1. Recalculate Balance tab row value 2. new column of Input&output grid | process unit， flow, | 更新 数值后台计算逻辑，Solver Penalty = Imbalance / Tolerance < Gross Error Threshold ? Imbalance / Tolerance: Gross Error Penalty 
84903: UI Integration: Expression Updates for Material Description, Material Parent, Tank Group Attribute | 1. 更新expression TankGroup().[AttributeName], Material().Description 2. 修改material 只有一个parent| 静态 defination + 动态感知 返回 attributeName | 
6723: Integration: Diagnostics UI |