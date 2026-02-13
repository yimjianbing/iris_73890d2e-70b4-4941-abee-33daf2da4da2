<title>Aime A2A One-Pager（WIP）</title>
<url>https://bytedance.larkoffice.com/wiki/UeGAwIHf1iQUwikBN2Ec5RpQnDf</url>
<content>
最近更新：2026-01-09

> Aime 入口：**https://aime.bytedance.net/**
> 

# 简介
## Aime A2A 是什么？
A2A（Agent-to-Agent）最初由 **Google** 提出，Aime 在其基础上做了扩展和增强。简单来说，A2A 让不同的智能 Agent 可以通过统一协议，方便地接入 Aime 平台，为用户提供多样化的服务。

与 Google 的 A2A 主要负责请求路由不同，Aime 的 A2A 不仅仅是“转发”，还支持任务流程的编排与把控，允许多个 Agent 协同完成复杂任务，实现全流程的治理与可观测性。

相比 MCP，A2A 支持更长的等待时长，分阶段返回中间结果，并且可以在任务执行过程中主动和用户交互、动态收集信息，适合需要多步处理或复杂决策的场景。

> **<font color="red">对于简单直给型任务，MCP 接入仍然是更低成本的选择</font>**
> 

![board_SGsvwGukshsnEab9pQxcV1XBnKe](board_SGsvwGukshsnEab9pQxcV1XBnKe.drawio)

## 接入 Aime A2A 的 ROI
对开发者而言，只需用司内的 Coze、LangGraph 或其他主流框架和工具搭建一个符合 A2A 协议的单轮 Agent，就能无缝集成到 Aime 平台，无需繁琐的对接和改造。

Aime 在整个任务流程中不仅仅做路由分发，更会主动检查、汇总结果，并在关键环节补位——比如有些配套流程（如会话管理、上下文压缩、数据下载、任务编排、文档生成等）

如果你的 Agent 不支持，Aime 会自动介入协同完成。这样，开发者只需要关注 Agent 的核心能力，剩下的流程和协作都由平台托管。

同时，Aime 还配备了完善的调试平台，方便你测试和优化 Agent，确保稳定运行并获得统一的结果展示和流量支持。

## 用户路径
<table header-row="true" col-widths="52,392,376">
    <tr>
        <td colspan="3">通过对话使用</td>
    </tr>
    <tr>
        <td>1</td>
        <td>用户选择智能体（可以选择多个）</td>
        <td>![图片](img_FvdMbDZMpocIi4xXf5McyadQnNS.png)</td>
    </tr>
    <tr>
        <td>2</td>
        <td>输入任务内容，点击发送</td>
        <td>![图片](img_JA7LbJZzQoV4CIxO7GbcIeLznfg.png)</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Aime 会根据任务的相关性，然后判断可以是否有合适的智能体，如果有，则会直接使用这个智能体。</td>
        <td>![图片](img_N1pkbeuQtoBOlWxzzFMc0tNTnDg.png)</td>
    </tr>
    <tr>
        <td colspan="3">**通过模板使用**</td>
    </tr>
    <tr>
        <td>1</td>
        <td>模板可以绑定 Agent，你可以在模板中强引导 Aime 使用某个 Agent，这样 Aime 就会在任务中使用某个 Agent。</td>
        <td></td>
    </tr>
</table>

## 已接入案例
<table header-row="true" col-widths="115,483,115,107">
    <tr>
        <td>案例名称</td>
        <td>简介</td>
        <td>POC</td>
        <td>手册</td>
    </tr>
    <tr>
        <td>文本用例生成</td>
        <td>基于 PRD/技术文档抽取测试点，生成checklist/测试用例并生成飞书文档。</td>
        <td>@(chenwenrui.cwr@bytedance.com)</td>
        <td>**链接**</td>
    </tr>
    <tr>
        <td>单测智能生成</td>
        <td>基于仓库/MR 计算差异，自动生成与修复用例，统计覆盖率并产出报告。</td>
        <td>@(denglingmin@bytedance.com)</td>
        <td>**链接**</td>
    </tr>
</table>

# 接入方式
<callout icon="rotating_light" bgc="1" bc="1">
当前 Aime A2A 还在小范围测试中，暂时不支持自助接入，如有需要，可以联系 @(zhujingyan.43@bytedance.com)
</callout>

[Aime Agent 接入文档](https://bytedance.larkoffice.com/wiki/QVW0w3ZMKiZRkAkOOZIcYUgwnDe)


</content>
