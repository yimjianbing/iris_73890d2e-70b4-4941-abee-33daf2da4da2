<title>Aime 工作流功能介绍</title>
<url>https://bytedance.larkoffice.com/wiki/BsMqwZwUdirlwFkTCj7cYjGVnDg</url>
<content>
<callout icon="bulb" bgc="3" bc="3">
你还在手动串联各个研发环节吗？
赶紧来试试 Aime 全新推出的**工作流功能** 🚀，集**模板串联、自动化执行、多轮对话、参数传递**于一身，让你的研发流程更高效、更智能！
[Aime - 项目空间使用手册](https://bytedance.larkoffice.com/docx/HC01dKOC3ohxomxwbG0c3VRVn9g?from=self_signature)
[Aime 项目空间：赋能团队研发提效](https://bytedance.larkoffice.com/docx/QtAjdMbSEo8x7HxgCOmcUJjqn8e)
任何问题 7 x 24 支持：@(xuezhongliang@bytedance.com)@(wuyunfei.vip@bytedance.com)
</callout>

# 功能介绍
Aime 工作流功能旨在将不同的 AI 环节进行串联，配置成自动化任务，满足用户在实际研发过程中的各种场景需求。无论是需求分析、技术方案生成，还是代码开发、测试部署，都可以通过工作流实现全流程自动化。

工作流功能的核心价值在于：

- **模板串联**：将原来的单点功能（模板任务）串联形成不同场景下的 SOP，提升场景可用性

- **灵活编排**：支持定时任务触发器、Codebase 触发器、Aime 模板任务、Bits 自由流水线等多种节点类型

- **智能执行**：单个节点支持多轮对话（上下文共享），支持多版本（上下文隔离）

- **参数传递**：跨节点实现上下文总结 + 产物传递（文件、图片、Code、链接）

- **效果调优**：支持从任意节点重跑，直到达到满意的效果，再开始后续任务

![图片](img_A4okbWYYSoyQsWxpEc2cqNjanGc.png)

# 使用方式
## 功能须知
<callout icon="saluting_face" bgc="2" bc="2">
1. 工作流功能目前已在 Aime 项目空间中灰度开放，用户需要在项目空间内使用。
</callout>

## 使用流程
工作流任务，需要基于工作流模版发起。

### 创建工作流模版
#### 进入 Aime 项目空间，点击首页的「新建工作流」按钮
![图片](img_AScubjvmIoHQLIx7H4kcZdJ1npd.png)

#### 进入工作流配置页面，拖拽需要的任务节点到画布中
目前节点类型支持 Codebase 触发器、定时任务触发器和 Aime 模版任务。

![图片](img_IdCcbb6bGoPiNtxT4yucBAiJn7c.png)

#### 定义节点的输入参数、输出参数
节点配置说明：
前置节点的输出参数，都可以被后续节点的输入参数引用。

- 输入参数，支持 2 种类型:
默认参数（固定值）与引用参数（引用前置节点的输出参数)。

- 输出参数，支持 5 种类型: 
文本：由模型根据当前任务的上下文进行总结，用户填写的`参数描述`将作为模型总结的重要依据。
代码、链接（飞书链接、网页链接等）、图片、文件（markdown、txt 文件等）：从当前任务生成的产物中进行筛选，`参数描述`将作为模型选择的重要依据。

- 节点执行人：以指定用户的身份运行当前节点的任务。

- 通知方式：当节点运行需要人工确认或任务完成后，消息通知的对象。

- 交互配置：节点执行完成后，是否需要人工确认执行任务的结果、任务的产物。**需要多轮对话、不断调优的场景**可以开启`执行完需要人工确认`；否则，当前节点执行完毕后，会自动开始运行下一节点。

![图片](img_PPqFbwuh4oBSAdxz9kicuVd0nvh.png)

#### 保存、发布工作流模版
建议修改模版的默认名称，提高辨识度。`保存`、`发布`工作流模版后，就可以基于该模版发起任务。

模版可见范围：

- 空间内可见：项目空间内所有人都可以基于该模版发起任务，且工作流任务默认空间内公开。

- 仅个人可见：仅模版创建者可基于该模版发起任务，且工作流任务默认仅个人可见。

![图片](img_RaJObLY2KoiQfJxrNNEcX2InnVc.png)

### 发起工作流任务
#### 模版编辑页面，发布模版后可以`立即运行`
![图片](img_JWG0bOzKQoaAYpxl4ricekMbnEd.png)

#### 项目空间首页，基于已有的模版发起任务
![图片](img_Ggd3bBd1iovPGmxhFCXcX2upnfh.png)

### 操作工作流任务
#### 人工确认与多轮对话
如果需要调整当前的产物，可以继续对话，直到符合预期再点击`确认`按钮进入下一节点。

![图片](img_QDbXbD7OzogJARxXzKecw6uQn5f.png)

#### 从指定节点开始重新运行
如果在工作流运行的过程中，发现前置节点的产物需要调整，可以从指定节点重新运行。支持 2 种方式：

- 保留前置节点的任务上下文

可以在历史节点中继续对话，修改历史产物。在完成修改后，点击`完成`按钮，将基于修正后的产物重跑后续节点。

![图片](img_GxR3bHbZJoxgeuxOIRmcNOgwnzh.png)

- 舍弃前置节点的任务上下文，完全重新开始

将从指定的节点创建新版本，开启全新的任务流程。未重跑的节点产物，可以继续被引用。

![图片](img_MCBZbVeJIoko2sxcY8qc76wKnVh.png)

只有节点的最新版本，才允许继续交互。

![图片](img_PoE0bwZvporzN5x4t1bcE9aynsc.png)

#### 取消运行中的任务
![图片](img_VfJbb5zbAof5YNxh9bFc6JM6nmb.png)

### 管理历史任务
#### 在「我的任务」页面，可以管理、查看个人的近期工作流任务
![图片](img_QgjebStXjo0lgNxULyJcgHehnEc.png)

#### 在「历史任务」页面，可以管理、查看个人与空间内公开的工作流任务
![图片](img_IYnRbbWmqo6jGYxtuEhcwTA0nNd.png)

# 线上典型使用姿势参考
<table col-widths="250,250,250,250">
    <tr>
        <td>场景</td>
        <td>细分场景</td>
        <td>案例介绍</td>
        <td>能力介绍</td>
    </tr>
    <tr>
        <td>**研发流程自动化**</td>
        <td>**需求到代码全链路**</td>
        <td>- **案例1:** 工作流串联 [需求](https://aime.bytedance.net/chat/474cb356-2f72-4771-9567-cb3aed740d9f?workflowRunId=59f1fc93-55cd-4b3a-ac31-0c2e6143c690)[分析-技术方案-代码开发](https://aime-boe.bytedance.net/chat/320e5720-de21-4f70-939a-d688de2fbfc3?workflowRunId=eee82393-e514-4cb0-8feb-1dd56a933d01)</td>
        <td>- **模板串联**：将需求分析、技术方案生成、代码开发等环节自动串联
- **参数传递**：前一环节的产物自动传递给下一环节</td>
    </tr>
    <tr>
        <td>**代码质量保障**</td>
        <td>**CodeReview 自动化**</td>
        <td>- **案例2:** [Codebase 触发器-CodeReview & 修复](https://aime.bytedance.net/chat/2bd8f975-be08-46f9-a3ae-2dedda4a5a2f?workflowRunId=d7924cc6-0311-4361-b2dd-b6ca7db1c75d)</td>
        <td>- **事件触发**：代码提交后自动触发 CodeReview
- **智能修复**：自动识别代码问题并提供修复建议</td>
    </tr>
    <tr>
        <td>**多轮交互优化**</td>
        <td>**复杂任务处理**</td>
        <td>- **案例3:** [多轮对话](https://aime-boe.bytedance.net/chat/ada841ee-3632-40ea-8fc3-b617d67e8099?workflowRunId=715f5cee-c9db-495e-9f09-a1787153ab5a)</td>
        <td>- **上下文共享**：单个节点支持多轮对话
- **效果调优**：支持从任意节点重跑</td>
    </tr>
</table>

# 常见问题
## Q1：工作流支持哪些节点类型？
**A：**目前支持定时任务触发器、Codebase 触发器、Aime 模板任务、Bits 自由流水线等多种节点类型，可以根据实际场景编排合适的工作流程。

## Q2：如何在工作流中传递参数？
**A：**工作流会自动实现跨节点的参数传递，包括上下文总结和产物传递（文件、图片、Code、链接等）。用户在配置节点时，可以通过参数引用传递需要的参数。

## Q3：工作流执行失败了怎么办？
**A：**工作流执行失败后，可以在「运行工单」页面查看详细的错误信息。支持从失败节点开始重跑，方便用户排查问题和优化流程。

## Q4：工作流功能是否支持自定义扩展？
**A：**是的，工作流功能后续将提供标准的集成方案和框架，适配业务个性化诉求。后续规划中，还将支持业务 Agent 的接入与能力扩展。

# 问题反馈渠道
可登记到文档：[Aime - 工作流功能 DogFooding 问题反馈](https://bytedance.larkoffice.com/wiki/D4ULwmorqiqcIYkC1ySc7PXZnuO?renamingWikiNode=false)

- 工作流模版配置问题联系 @(wuyunfei.vip@bytedance.com)

- 工作流任务执行问题联系 @(xuezhongliang@bytedance.com)

- 产品诉求及其他联系 @(zhujingyan.43@bytedance.com)@(litengfei@bytedance.com)




</content>
