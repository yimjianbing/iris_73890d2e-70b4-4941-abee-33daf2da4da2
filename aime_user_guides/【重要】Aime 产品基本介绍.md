<title>【重要】Aime 产品基本介绍</title>
<url>https://bytedance.larkoffice.com/wiki/SHBrwmkuOijz0hkFekWc84cVnVd</url>
<content>
最近更新：2026-01-09

<callout icon="man-surfing" bgc="5" bc="5">
产品官网：
- https://aime.bytedance.net/
- https://aime.tiktok-row.net/（访问全球工具的）
***Ai~me（发音:艾米），即AI和我，希望Aime可以融入到每一位字节同学的工作生活中***
> 受限于资源，内测名额逐步放量，产品持续在优化，如有不足欢迎反馈，敬请谅解
> 
</callout>

# Aime 是什么？
Aime 是专为字节同学打造的AI Agent工作平台，面向工作场景，集成了字节内部常用工具，帮助大家高效完成各类繁琐重复的任务，包括但不限于：写代码、分析数据、做调研、写文档 等

与Aime一起，将会逐渐开启异步办公新模式~[Aime项目组是如何实践异步办公的【随笔】](https://bytedance.larkoffice.com/docx/B77Bd0PxQopil9xGBzlcV6HdnNg)。

# 主要特点 - 异步办公
> for研发同学：你在开会时,Aime在帮你写代码；你去下楼吃午饭时,Aime在帮你做代码CR,
> 
> for非研发同学：你在开会时，Aime在帮你做竞品调研；你去楼下吃午饭时，Aime在帮你复盘活动数据；
> 

你们独立进行各自的任务，直到Aime通知你完成了再回来验收。这就是Aime的异步办公的新体验。Aime有如下特点：

- **更智能的Agent，多能力融合**：自主规划完成长时间的复杂任务，融合了代码开发、数据分析、调研分析、写文档等多种能力

- **为ByteDancer量身定制**：集成字节内部工作的常用工具并深度优化，包括但不限于：
	- 通用工具：飞书文档&表格、wiki知识库
	- 数分平台：Meego、风神、DevMind
	- 研发平台：Codebase、Slardar&Argos&PerfSee 

- **从模板发起任务**：内置了大量常见模板，可以快速发起复杂任务，模板可以自定义、收藏和分享，打造你自己的AI工作台~

- **丰富的开放生态**：支持用户接入自定义MCP、自定义快捷任务，未来会接入垂类Agent

# 核心场景
当你去开会、喝咖啡或专注在核心工作中的时候，Aime可以帮你完成类似下面的任务：

## 代码&研发类任务
写demo、修bug、CodeReview，这些小活儿都可以交给Aime，异步帮你干，你来检验Aime的工作结果

<grid cols="2">
<column width="47">
  修复Slardar线上客户端异常崩溃（[回放](https://aime.bytedance.net/share/12ed72e2-92de-42e6-afb0-203475b8ae7a)）
</column>
<column width="52">
  批量 lint 问题修复 （[回放](https://aime.bytedance.net/share/e11282c9-d88b-48da-af15-01a6af010cd3)）
</column>
</grid>

<grid cols="2">
<column width="50">
  MR review（[回放](https://aime.bytedance.net/share/eca38cbe-a511-427e-99ce-d0b9665cc1fc)）
</column>
<column width="49">
  执行接口测试并分析（[回放](https://aime.bytedance.net/share/b4a7eaa3-3347-4484-b800-6d77fa87e41a)）
</column>
</grid>

## 数据分析类任务
- Aime 可以为你进行数据打标，Oncall分析。

- 还可以为你生成完整的分析报告，如：[业务定容率效能报告（2024.11-2025.06）](https://bytedance.larkoffice.com/wiki/RrKUwQYzwiWcidkyDfIcZ9Oxnqf)

> 当前支持的数据源有：风神，Meego，Oncall，DevMind，Tea，Libra
> 
> 后续还会陆续支持：Dorado，
> 
> 我们也支持自定义的数据，通过 MCP 的方式将数据源提供给我们。
> 

<grid cols="2">
<column width="45">
  数据打标&Oncall分析
</column>
<column width="54">
  分析报告：业务定容率效能
</column>
</grid>

<grid cols="3">
<column width="33">
  分析报告：产品 NPS 分析
</column>
<column width="33">
  分析报告：不同职场审核情况
</column>
<column width="33">
  分析报告：支付GMV的相关性
</column>
</grid>

<grid cols="2">
<column width="50">
  分析报告：商圈洞察分析
</column>
<column width="49">
  分析报告：抖音推荐服务成本变化分析
</column>
</grid>

## 调研&检索任务
-  快速从大量数据和分散系统中发现所需关键信息。

<grid cols="2">
<column width="50">
  技术学习材料生成（[回放](https://aime.bytedance.net/share/1571975d-01f1-491d-bcf1-3f700dfd0259)）
</column>
<column width="50">
  网址资讯总结（[回放](https://aime.bytedance.net/share/ee8f0051-d5ea-4053-b549-1ead6a322b11)）
</column>
</grid>

-  AI辅助撰写各类文档、分析及创意方案，提升内容生产效率。

<grid cols="2">
<column width="50">
  竞品调研（[回放](https://aime.bytedance.net/share/203b594e-7dd7-4376-9aa1-cc0bdd9b6665)）
</column>
<column width="49">
  产品功能埋点方案设计
</column>
</grid>

## 大卫和小美的区别
**大卫（David/invited_expert）** 是专家级 AI Agent，定位为"受邀专家"。他擅长多角度分析、深度推演，特别适合处理研发与代码相关任务。目前大卫已支持 auto 模式，既可以快速回答简单问题，也能深度处理复杂任务，具备更强的推理能力和专业水平。**建议优先使用大卫处理各种类型的任务**，他是生产环境中的全能首选。

**小美（XiaoMei/newbie）** 是新手级 AI Agent，定位为"入门助手"。她擅长高效执行、结构清晰，特别适合处理调研与文档生成相关任务。小美在处理常规任务时需要更详细的指导和示例，能够快速响应基础需求。**需要注意的是，随着大卫 auto 模式的完善，小美将逐渐下线，建议新用户直接使用大卫以获得更好的体验。**

# 内测群
Aime还在内测中，持续优化，如有不足欢迎反馈，敬请谅解


# **浅谈愿景和设计理念**

古希腊哲学家阿基米德曾说：“给我一个支点，我就能撬起整个地球。” 同样地，我们相信“给我一台电脑，AI 就能改变世界。”因此，我们打造了这个产品 —— 一个以 AI 为核心，配备虚拟化操作系统、控制台、浏览器和代码编辑器的产品，让 AI 能自由探索世界，这正是它与传统“Copilot”的最大不同。
Think Big，Start Small，Aime 的征程从助力每位 ByteDancer 开始：处理重复琐碎的任务、修复 Bug、简单数据分析等。尽管仍处于早期阶段，但通过持续迭代，它将不断突破边界，变得更加强大。让我们一起见证它的成长！


</content>
