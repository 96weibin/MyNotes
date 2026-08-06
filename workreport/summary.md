# PI2 - PI3 工作汇报

## 汇报摘要

本阶段工作聚焦两个方向：

1. 完成 Aura Diagnostics 从基础展示、数据集成到信息准确性和体验优化的交付闭环。
2. 推进 AUS NLE 能力落地，完成 Squaring Grid 展示、状态控制、导出、操作追溯，并持续对齐 AUP 与 AUS 的行为。

## 核心数据

阶段 | Story | Story Point
-|-:|-:
PI2 | 5 | 19
PI3 | 3 | 18
合计 | 8 | 37

## 主要交付

### PI2: Aura Diagnostics 与表达式能力

- 完成 Diagnostics UI 主链路：详情面板的 warning/error 信息展示、A-bar 告警图标和数量联动、Diagnostics 导航及 toast 提示。
- 接入 diagnostics GraphQL 数据，在 Case 切换时刷新，保障 API 异常场景下 UI 稳定。
- 更新 Diagnostics 的信息模型和视觉呈现：支持 Warning、Error、Assumption 分类及 Type badge，并与最新设计保持一致。
- 统一 Balance Tab 中 Solver Penalty、Loss/Gain 等字段语义，展示真实 solver penalty，并补充 tooltip 和调整列。
- 扩展表达式编辑器，支持 Material Description、Material Parent、Tank Group 及其属性；同时增加 Material Parent 的单选校验。

### PI3: NLE in AUS

- 在 Squaring Grid 中提供 NLE 列和行级开关；未解析变量时禁用操作，并通过 tooltip 展示 NLE equation、expression、variable mapping 与 unresolved 信息。
- 补齐 Simulation Configuration 和 XLP 导出能力，优化 NLE Term/NLE Expression 列布局与可见性，方便用户分析和导出配置。
- 将 NLE Term 启用/停用操作写入 Simulation Log，提升配置变更的可追溯性。
- 持续对齐 AUS/AUP 的 NLE 行为，包括状态更新返回契约、Simulation 后 Grid 刷新和变量列表一致性。
- 修复 Simulation Matrix 重复追加变量、Grid 过滤后表头未刷新、NLE 状态变更后 Matrix 未更新等可用性问题。

## ATL 团队协作与交付推进

从 PI2 开始承担 ATL 工作，除个人功能交付外，负责组织团队的敏捷协作节奏和交付信息同步：

- 主持 Iteration Review & Planning：走查 Iteration Board，确认 Story 的完成、关闭或 carry-over 结论；组织 Demo，并衔接下一迭代的工作规划。
- 主持 Weekly Sync：同步团队进度、测试资源和优先级；明确高优先级测试工作、剩余测试范围和跨迭代安排。
- 组织 Breakout Session：提前讨论 Release 风险、前后端依赖、UI mockup、权限模型和 NLE Catalog 等开放问题，推动相关角色达成下一步行动。
- 建立并维护 Daily Meeting、Weekly Sync、Review & Planning 模板，统一记录完成项、风险、blocker、owner、决策和 follow-up，帮助团队将讨论转化为可跟踪行动。
- 在 PI3 Review 中完成 AUS NLE 功能 Demo，并同步 AUP/AUS 对齐、测试风险和后续 Story 安排，支持团队对交付范围形成共识。

## 质量与缺陷收口

本阶段完成 5 个可追溯 ADO 编号的 Bug 修复：

阶段 | ADO Bug | 主要修复方向
-|-|-
PI2 | 107614 | AURA Solver Penalty 的显示和计算
PI2 | 107667 | Event Solver Penalty 在 Gross Error Threshold 边界场景下的计算
PI2 | 105219 | Bug code review 问题收口
PI2 | 111293 | AURA V15 Post Development Bug
PI3 | 124140 | AUP NLE UI 显示问题及后续收口

除上述 ADO Bug 外，还持续处理了 Diagnostics UX、NLE 日志保存、Grid 刷新和过滤等稳定性问题，并完成相关 BDD 修复与回归维护。

## 进行中与下一步

- 持续验证 NLE 状态变更、Simulation Matrix 刷新和变量同步在复杂场景下的一致性。
- 跟进 NLE 相关导出、日志和 Grid 交互的回归，确保新能力在真实配置场景下稳定可用。

## 建议口头汇报

> 这两个 PI 我主要完成了 Diagnostics 和 NLE in AUS 两条功能线。PI2 聚焦 Aura Diagnostics，从告警展示、数据集成到错误和假设分类都完成了闭环，同时也把 Solver Penalty 的计算边界和表达式能力做了完善。PI3 聚焦 NLE 的实际可用性，完成了 Grid 中的状态控制、信息展示、导出和操作日志，并持续解决 AUS/AUP 对齐、状态切换后刷新和变量重复等问题。整体负责 8 个 Story、37 个 points，均已完成；另外完成了 5 个有 ADO 编号的 Bug 修复。从 PI2 开始，我也承担 ATL 工作，组织 Review & Planning、Weekly Sync 和 Breakout，推动团队对交付结论、测试优先级、风险和依赖达成共识并落实 follow-up。后续会继续做 NLE 相关场景的稳定性回归。
