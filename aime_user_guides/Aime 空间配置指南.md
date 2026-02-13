<title>Aime 空间配置指南</title>
<url>https://bytedance.larkoffice.com/wiki/R8YIw8XXLixg3okhYfpcSv4Zn3g</url>
<content>
<!-- BLOCK_1 | Serqdg67KoMuXGx5PKKcW6oFn8g -->
<callout icon="bulb" bgc="2" bc="2">
空间配置是释放 Aime 团队协作与空间任务执行潜力的关键。通过精准配置空间 “资源”与“知识”，你可以将分散的内部平台、代码仓库、文档库与任务规范整合为 Aime 可理解、可调用的信息，从而显著提升业务场景下执行任务的准确性、稳定性与效率。
推荐阅读：
[告别低效重复，让 Aime 精准“听懂”你的指令：用户自定义知识使用指南](https://bytedance.larkoffice.com/docx/TrRzdMYZZoyYoQx6XoYcni1Pnfe)、[Aime Skill 指南](https://bytedance.larkoffice.com/wiki/BSVVwNRRdi6TDSkTHJNcUDiznbe)
</callout>

<!-- END_BLOCK_1 -->
<!-- BLOCK_2 | IEi8dWN3JovkNrxFMhLcEdhMnFd -->
## 关键信息与注意事项
<!-- END_BLOCK_2 -->
<!-- BLOCK_3 | I6cKd1J4aoaAFCxlNC7c4r4pnab -->
- **概念边界**：
	- **资源**：分为信息源与平台两大类，Aime 通过连接这些资源进行跨平台异构信息的深度检索、分析和联动。
		- 信息源：指代码仓库、TCE 服务、测试用例、文档库等事实性“信息源” （注：个人空间暂时仅支持配置文档库资源，后续将逐步支持开发配置其他类型资源）
		- 平台：指 Meego、Bits 等可双向触发功能联动的“平台”
	- **知识**：指用户自定义的“指导规则”，是任务执行时具有最高优先级的行为准则。它告诉 Aime“应该怎么做”，更侧重于流程、规范和约束。

<!-- END_BLOCK_3 -->
<!-- BLOCK_4 | Xx7wdkllHoUcVrx6ObUcYfvPn8g -->
- **同步与安全**：
	- **更新机制**：文档库资源将根据文档修改情况自动定时更新，也支持手动更新。知识中引用的云文档内容变更后，也建议手动触发更新，以保证信息同步。
	- **权限风险**：文档库中的文档导入后会授权给 Aime 离线处理，导入后空间内所有成员可消费文档内容，可能存在数据越权的风险。请在导入前评估文档内容的敏感性，谨慎操作。

<!-- END_BLOCK_4 -->
<!-- BLOCK_5 | EwLddFGGJoGc4MxEYjncsKf1nIv -->
- **权限与可见性**：
	- **资源配置**：空间管理员与成员均可配置和导入各类资源。但请注意，部分资源（如代码仓库、TCE 服务）在创建 Aime 任务消费时，Aime 会校验当前操作者的个人权限以提供服务。
	- **知识配置**：空间管理员可以创建“空间公开”的知识，默认对所有空间成员启用；普通成员只能创建“个人可见”的知识。用户可自行选择是否要启用或停用某条知识。

<!-- END_BLOCK_5 -->
<!-- BLOCK_6 | Gp8fdcrbhodvm8xq6RScKLSdnsg -->


<!-- END_BLOCK_6 -->
<!-- BLOCK_7 | T8VqdGTDroQt73xzdggc917TntI -->
## 快速上手
<!-- END_BLOCK_7 -->
<!-- BLOCK_8 | H3KudV43ToxbDyxuubBcUmuanme -->
> 本章节将引导你完成空间配置的核心流程。
> 

<!-- END_BLOCK_8 -->
<!-- BLOCK_9 | AZkPddHsPor8KmxHgrpcVv3xnDd -->
### 步骤一：进入配置页面
<!-- END_BLOCK_9 -->
<!-- BLOCK_10 | JaQidNzw7o9ZP6xutm1czD9tnkb -->
在 Aime 首页，选择你的目标空间，并单击空间名称右侧的 **配置** 按钮，即可进入空间的基础信息配置页面。仅管理员可操作，普通成员仅可查看空间的基本信息。

<!-- END_BLOCK_10 -->
<!-- BLOCK_11 | DrPldyawvos5pjx2SYTc0j6gnhg -->
![图片](img_A4GmbUzNOon08BxJZivcD9elnCN.png)

<!-- END_BLOCK_11 -->
<!-- BLOCK_12 | WniFdrtSdo3pp3xfhOFchKqIncg -->
### 步骤二：资源配置
<!-- END_BLOCK_12 -->
<!-- BLOCK_13 | BqEhdTH7Qo54pxxmchgc4cyYnug -->
> 资源是希望 Aime 在执行任务时能够访问和理解的外部信息源。合理的资源配置是提升任务质量的基础。
> 

<!-- END_BLOCK_13 -->
<!-- BLOCK_14 | GF19dzABEohL0axXfZEcyna0nVh -->
![图片](img_KB4cbDuBNoSV9cxrUnUcIQLTn9r.png)

<!-- END_BLOCK_14 -->
<!-- BLOCK_15 | U8FpdNPnjoZswfx9PoocuHwpnKd -->
点击左侧导航栏中的 **资源配置** 。根据你的团队需求，连接项目相关的代码仓库、TCE 服务、Meego 空间、测试用例库和文档库。（注：个人空间暂时仅支持配置文档库资源，后续将逐步支持开发配置其他类型资源）

<!-- END_BLOCK_15 -->
<!-- BLOCK_16 | PI41dVMd6oPbSvx5uufcx5gXnvf -->
<table header-row="true" col-widths="100,112,250,250,250">
    <tr>
        <td>**资源类型**</td>
        <td>资源名称</td>
        <td>字段说明与操作</td>
        <td>配置权限要求</td>
        <td>常见问题与最佳实践</td>
    </tr>
    <tr>
        <td rowspan="6">**信息源**</td>
        <td>**文档库**</td>
        <td>支持上传或链接飞书文档、表格、多维表格以及整个 Wiki 知识库。
Aime 会将其作为背景信息，在任务执行的过程中基于文档信息切片触发检索。</td>
        <td>录入人需要具备文档的访问权限。
上传的文档会转存并切片，空间内所有成员均可检索，存在越权风险，请谨慎评估。</td>
        <td>**最佳实践**：
- 在指令中通过“根据知识库/文档 xxx”来主动触发，以提升命中准确性
- 避免导入大量低质量、过期的文档，这会干扰检索结果。
- 文档库支持自动更新，但重要变更后建议**手动更新**以保证时效性。</td>
    </tr>
    <tr>
        <td>**代码仓库**</td>
        <td>填入 Git 仓库地址。
Aime 将能够理解代码结构、分析代码功能，并用于代码生成、修复、影响面分析等多种研发场景。</td>
        <td>录入人需要具备该代码仓库的 `clone` 权限。</td>
        <td>**最佳实践**：优先添加团队核心业务相关的代码仓库。对于大型单体仓库，确保 Aime 能够访问你关心的主要模块。</td>
    </tr>
    <tr>
        <td>**TCE 服务**</td>
        <td>填入服务的 PSM 名称。
Aime 可以获取服务的接口定义、调用关系、SCM 信息和线上调用链，用于 LogID 排障、接口稳定性分析等。</td>
        <td>录入人需要具备该 TCE 服务的**可读**权限。</td>
        <td>**常见问题**：如果服务信息不全，请检查你的 TCE 权限是否正确。</td>
    </tr>
    <tr>
        <td>**Meego**</td>
        <td>粘贴 Meego 空间或特定工作项的 URL 进行关联。
Aime 可以理解需求、缺陷等信息，并与研发任务联动。</td>
        <td>录入人需要具备对应 Meego 空间的**访问权限**并完成授权。</td>
        <td>**最佳实践**：将整个团队的 Meego 主空间进行关联，而非零散的工作项，以保证信息覆盖的全面性。</td>
    </tr>
    <tr>
        <td>**测试用例**</td>
        <td>填入 Bits 测试用例库的空间地址。
Aime 可以学习现有的测试用例，从而在面对新需求时生成更贴切、更完备的测试用例。</td>
        <td>录入人需要具备该 Bits 空间的**阅读**权限。</td>
        <td>**最佳实践**：导入覆盖核心业务流程的测试用例库，有助于 AI 更好地理解业务逻辑。</td>
    </tr>
    <tr>
        <td>**风神**</td>
        <td>**支持导入风神仪表盘或可视化查询的 URL。**
Aime 会每日前置更新数据，用于在数据问答场景中快速响应。</td>
        <td>录入人需具备对应仪表盘/查询的**访问权限**并完成登录授权。
- 暂不支持录入未保存的可视化查询</td>
        <td>**最佳实践**：优先导入日常高频使用的、固定的数据看板，以便 Aime 学习和加速。</td>
    </tr>
    <tr>
        <td>**平台配置**</td>
        <td>**Meego**</td>
        <td>复制 Meego 项目链接以关联 Meego，通过 Meego 平台 Aime 官方插件获取全部需求和缺陷流转信息。在 Aime 配置不同节点的绑定模板后可通过绑定的模版一键发起任务。</td>
        <td>录入人需要具备 Meego 空间的访问权限。</td>
        <td>**最佳实践：**
- 在需求设计节点配置关联 Aime PRD 设计/review 模板，帮助查漏补缺、提供建议
- 技术开发节点，结合代码仓库和历史技术方案，生成符合团队技术栈和开发规范的前端技术方案，包含架构设计、技术选型、实现细节等</td>
    </tr>
</table>

<!-- END_BLOCK_16 -->
<!-- BLOCK_17 | GBp2diIH8orC8dxUlObc0Sb2nic -->
<grid cols="2">
<column width="46">
  ![图片](img_ADbAbZiEAoJIdYxzXV5cbvdhnDc.png)
</column>
<column width="53">
  ![图片](img_IjSMbiGYYokIsXxE8XVc60cunPh.png)
</column>
</grid>

<!-- END_BLOCK_17 -->
<!-- BLOCK_18 | TBggd8rEWo7XPLx7rGLcGs3Kn0b -->


<!-- END_BLOCK_18 -->
<!-- BLOCK_19 | Ok7ZdVPWjoEuBqxrnBycQBCZnsh -->
### 步骤三：知识配置
<!-- END_BLOCK_19 -->
<!-- BLOCK_20 | Ke9ldobq5oFz5OxOoAyclMaqnyc -->
> “自定义知识”是你为 Aime 设定的、具有**最高优先级**的指导规则。它与“文档库”资源的核心区别在于：
> 
> - 文档库（被动检索）：如同一个庞大的图书馆，Aime 会将文档内容切片处理后，在需要时根据任务语义去“搜索”相关信息作为参考。它回答的是“是什么”的问题。
> 
> - 用户自定义知识（主动遵循）：<font background_color="medium_gray">如同下达给 Aime 的“军规”，只要满足触发条件，Aime 就必须“遵循”其内容执行任务</font>。它回答的是“应该怎么做”的问题。
> 
> **<font background_color="light_red">知识简介与最佳实践指南：</font>**[告别低效重复，让 Aime 精准“听懂”你的指令：用户自定义知识使用指南](https://bytedance.larkoffice.com/docx/TrRzdMYZZoyYoQx6XoYcni1Pnfe)
> 

<!-- END_BLOCK_20 -->
<!-- BLOCK_21 | UeeIdeZZJoKXJCxrZRGcqOddnpe -->
<grid cols="2">
<column width="28">
  ![图片](img_LBuqb9rJDo5OqYx8rPEcQMqunTc.png)
</column>
<column width="71">
  侧边栏切换到 **知识配置**。在这里，你可以将团队的工作流程、业务规范、特殊指令等沉淀为结构化的知识。
  通过配置知识，你可以约束和引导 Aime 的行为，使其更符合团队规范。
</column>
</grid>

<!-- END_BLOCK_21 -->
<!-- BLOCK_22 | YcsGdDP85o88u4xnhWIcz7m1nQe -->
<table header-row="true" col-widths="104,282,584">
    <tr>
        <td>配置项</td>
        <td>字段说明与操作</td>
        <td>最佳实践或说明</td>
    </tr>
    <tr>
        <td>**知识名称**</td>
        <td>为你的知识规则起一个简洁、明确的名称，便于后续管理和识别。</td>
        <td>- 字符数上限 50
- **示例**：“代码提交规范”、“业务知识”、“全局任务通用规则”……
<grid cols="2">
<column width="50">
  - Goodcase：
  	- 代码评审要点清单-Android
  	- 长文分块-规范类
</column>
<column width="50">
  - Badcase：
  	- 代码评审要点清单
  	- 长文处理
</column>
</grid></td>
    </tr>
    <tr>
        <td>**知识内容**</td>
        <td>填写规则的具体描述。支持纯文本、上传附件（[skill.zip](https://bytedance.larkoffice.com/wiki/BSVVwNRRdi6TDSkTHJNcUDiznbe)）或引用飞书云文档。
**这是知识的核心，需要清晰、准确。**
<grid cols="2">
<column width="70">
  注：飞书云文档类型将自动检测文档更新的情况保持同步更新，若有即时更新的需求，请点击 “… - 更新文档” 
</column>
<column width="30">
  ![图片](img_ZLihbuHMmoVOnmxYGVrc5j4Rnac.png)
</column>
</grid></td>
        <td>- 内容的表述需要清晰、明确；更小、更具指导性的片段知识效果更佳
- 对于复杂的流程，建议使用云文档承载，并在知识内容中引用其链接。
<grid cols="2">
<column width="63">
  - Goodcase：
  	- 排期节点查询-抖音：
  	关键步骤要点：1) 获取需求ID/链接；2) 查询节点与估分；3) 输出节点名称、状态、负责人、预计完成时间。
  	- 代码评审要点清单-Android：
  	总述：帮助在 Java/Kotlin 工程进行评审时快速列出关键检查项。
  	关键步骤要点：1) 结构/依赖变更；2) 线程与生命周期；3) 性能与内存；4) API 兼容；5) 安全与隐私。
</column>
<column width="36">
  - Badcase：
  	- “这是关于排期的知识，按情况处理。”（缺少范围、触发条件、步骤、输出定义）
  	- “注意质量与规范。”（泛化描述，无法操作）
</column>
</grid></td>
    </tr>
    <tr>
        <td>**应用场景 (use_when)**</td>
        <td>定义这条知识在何种情况下被触发。你可以手动编写，也可以在填写完“知识内容”后，点击 **AI 自动生成**来快速填充。</td>
        <td>**手动编写示例**：
- `当任务是“代码审查”或“Code Review”时` (关键词触发)
- `当任务涉及到修改数据库表结构时` (场景描述触发)
**最佳实践**：`use_when` 的描述应尽可能精准，避免过于宽泛导致不相关的任务也命中规则。
<grid cols="2">
<column width="62">
  - Goodcase：
  	- 当需要查询抖音 Meego 需求的排期节点或估分信息时；输入包含需求ID或链接
  	- 当编写周报并需要自动生成结构化提纲（包含目标、进展、风险）时；适用个人或团队周报
</column>
<column width="37">
  - Badcase：
  	- 需要查询排期
  	- 写周报
</column>
</grid></td>
    </tr>
    <tr>
        <td>**可见范围**
（仅项目空间内有区分）</td>
        <td>- **空间公开**：对项目空间内所有成员可见并生效。（仅管理员可创建）
- **个人可见**：仅对创建者本人可见并生效</td>
        <td>团队通用的规范（如研发流程、部署手册）适合设为“空间公开”；个人工作习惯或临时调试性指令则建议设为“个人可见”</td>
    </tr>
    <tr>
        <td>**启停**</td>
        <td>- **启/停**：所有用户都可以对选择启用或弃用空间内配置的知识，以调节任务效果</td>
        <td>- 空间公开的知识将默认设置对全员启用，用户可自行判断是否停用/启用。
- 对于暂时用不到或已过期的知识，应及时停用或删除，避免对任务产生干扰。</td>
    </tr>
    <tr>
        <td>**知识检测**</td>
        <td>- **检测机制**：保存时会进行安全、冲突、重复、过期检测。</td>
        <td>导入失败时，系统会明确提示失败原因，请根据提示调整后重新提交。</td>
    </tr>
</table>

<!-- END_BLOCK_22 -->
<!-- BLOCK_23 | RGgddVRnjoEMZuxn0ZzczniwnOc -->
注：单个空间允许录入 1-40 条空间公开的知识，每位成员可录入 1-10 则个人可见的知识；请合理规划并及时更新

<!-- END_BLOCK_23 -->
<!-- BLOCK_24 | H13wdmlm0olkVNxan4Bc3s3CnXb -->
#### 知识常见示例
<!-- END_BLOCK_24 -->
<!-- BLOCK_25 | JtL8dUdqNoDKQ0xY30Zcn7zanNc -->
> **Aime SKILL 指南：**[Aime Skill 指南](https://bytedance.larkoffice.com/wiki/BSVVwNRRdi6TDSkTHJNcUDiznbe)
> 
> - 什么是 Skill  https://support.claude.com/en/articles/12512176-what-are-skills
> 
> - 使用 Skill https://support.claude.com/en/articles/12512180-using-skills-in-claude
> 
> - 如何创建自己的 Skill https://support.claude.com/en/articles/12512198-how-to-create-custom-skills
> 
> - Skill Market：http://skillsmp.com/
> 

<!-- END_BLOCK_25 -->
<!-- BLOCK_26 | XY7nd7msuoEc6IxhqyFcLUHunWe -->
<table header-row="true" col-widths="187,554,271">
    <tr>
        <td>知识名称（skill-name）</td>
        <td>知识内容（SKILL.md）</td>
        <td>使用时机（skill-description）</td>
    </tr>
    <tr>
        <td>**技术方案撰写**</td>
        <td>- **先读代码与服务调用链**： 确认相关代码库与服务拓扑，理解现有实现。
- **明确非功能性需求**：识别 PRD 中遗漏的性能、SLA、安全、合规指标。
- **梳理影响范围**：定位当前需求可能影响的逻辑模块与上下游依赖。
- **查找相似方案**：在内部查找解决相似问题（如高并发、数据一致性）的技术方案或代码库。</td>
        <td>- 当需要撰写技术方案时
- 需要为新功能/模块编写技术设计
- 技术选型/架构设计</td>
    </tr>
    <tr>
        <td>**数据库慢 SQL 诊断**</td>
        <td>- **获取慢 SQL 与表信息**：必须通过 `rds` 工具获取慢 SQL 详情与相关表结构。
- **结合代码逻辑分析**：定位执行该 SQL 的服务与代码，理解业务上下文。
- **分析执行计划**：检查索引使用情况、扫描行数等，找出性能瓶颈。
- **提出优化建议**：给出修改索引、重写 SQL 或调整代码逻辑的具体建议。</td>
        <td>- 当需要诊断慢 SQL 时
- 分析数据库性能问题
- 优化慢查询</td>
    </tr>
    <tr>
        <td>**测试用例复用**</td>
        <td>- **完整查看用例集**：获取相关功能的测试用例集脑图。
- **记录可复用链路**：提取可复用的测试链路与关键节点，记录其脑图结构。
- **避免无关信息**：不要引入通用的审计、性能等非直接相关的测试点。
- **聚焦核心变更**：基于现有用例，补充针对新需求的测试场景。</td>
        <td>- 当需要为新功能设计测试用例时
- 评估已有测试覆盖范围
- 补充回归测试用例</td>
    </tr>
    <tr>
        <td>**Meego 工作项分析**</td>
        <td>- **用 meego 工具读取详情**：禁止使用 browser，优先用 meego 工具获取工作项内容。
- **识别关联 MR 与文档**：通过 `knowledge_graph` 找到关联的 Merge Request；使用 `lark` 工具读取关联的飞书文档。
- **禁止 browser 获取飞书文档**：严格遵守规范，避免使用浏览器访问飞书文档链接。
- **分析完整上下文**：综合工作项、MR、文档信息，全面理解需求。</td>
        <td>- 当需要分析 Meego 需求/缺陷时
- 理解工作项背景与关联信息
- 评估需求范围与影响</td>
    </tr>
    <tr>
        <td>**代码最小改动**</td>
        <td>- **先看上下文与依赖**：在修改前，先查看文件上下文、导入语句及相关依赖，理解代码框架与惯例。
- **遵循库/框架惯例**：以最符合项目既有风格的方式进行修改。
- **补齐单元测试**：对修改或新增的代码，编写相应的单元测试以保证质量。
- **避免引入新库**：优先使用代码库中已有的工具或库，避免不必要地增加新依赖。</td>
        <td>- 当需要修改现有代码时
- 修复 bug 或添加小功能
- 代码重构</td>
    </tr>
    <tr>
        <td>**Claude Skills 示例 (可复用技能包)**
- `name` 最多 64 个字符</td>
        <td>- `SKILL.md` 主体内容应保持简洁，通常低于 5k tokens
- **常用技能 (document-skills)**: 提供创建和编辑 Office 文档（如 `.docx`, `.pptx`, `.xlsx`）和 PDF 的能力。
- **品牌规范 (brand-guidelines):** 应用官方品牌颜色、字体和 Logo，确保输出内容视觉统一。
- **Web 应用测试 (webapp-testing):** 使用 Playwright 验证前端功能、调试 UI 并捕获浏览器日志。
- **自定义的SKill包：**处理skill复用流程，加快执行效率，提示稳定性
> 查看更多：
> 
> - 官方案例：https://github.com/anthropics/skills
> 
> - 官方文档：https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices
> </td>
        <td>- `description` 最多 1024 个字符，不能包含 XML 标签， 应说明该技能（Skill）的功能的和使用场景
- 标准化文档生成: 当需要批量创建或编辑符合特定模板的 Word 文档、PPT 或 Excel 表格时。
- 确保品牌一致性： 在生成对外宣传材料、报告或演示文稿时，确保符合公司品牌规范。
- 自动化前端测试: 在开发流程中，自动执行 Web 应用的功能和 UI 测试。</td>
    </tr>
</table>

<!-- END_BLOCK_26 -->
<!-- BLOCK_27 | PvhAdqrZAoFQNQxVXL0cfNIlnnc -->
### 步骤四：验证与日常维护
<!-- END_BLOCK_27 -->
<!-- BLOCK_28 | KSqGdAlrmoRz3UxVPrecDdignNd -->
![图片](img_SJZFbBg5GoO7gexi9fec64pOnCN.png)

<!-- END_BLOCK_28 -->
<!-- BLOCK_29 | J26GdFtRIo4UAlxf6Ydcduj6nof -->
配置完成后，可在任务详情页的 Aime 执行过程中查看“本次命中的知识/规则”与召回的文档库文档片段信息等。

<!-- END_BLOCK_29 -->
<!-- BLOCK_30 | FmVZdYQREotnVRxEI67cnaIgnId -->
消费知识的方式：

<!-- END_BLOCK_30 -->
<!-- BLOCK_31 | MfAhd0zz7oQa4Sx3rFocdDMtn4d -->
1. 只要在知识配置中启用知识，Aime 就会根据填写的 “使用场景/描述” 字段自主判断需要召回的知识

<!-- END_BLOCK_31 -->
<!-- BLOCK_32 | B8RMdOtNXol53QxJW7UcgxAcnoc -->
2. 若已明确本次任务中需要调用的知识，可在会话框中主动 @ 启用的自定义知识

<!-- END_BLOCK_32 -->
<!-- BLOCK_33 | Zx1fdmaydozxogx3JpzcWo1WnOO -->
![图片](img_DhmsbhS18oRUoqx26LucpKQ4npg.png)

<!-- END_BLOCK_33 -->
<!-- BLOCK_34 | M4AkdGv2qoEEVAxsopRcnbK2nwc -->
日常工作中，请关注知识的有效性，及时停用或更新过期的知识，并根据团队需求补充新的资源。

<!-- END_BLOCK_34 -->
<!-- BLOCK_35 | NGOddulF5oE5joxp8dkceUmWngf -->


<!-- END_BLOCK_35 -->
<!-- BLOCK_36 | ATOmdRuMloNtEFxluXHcAzjtnMb -->
## 常见问题 (FAQ)
<!-- END_BLOCK_36 -->
<!-- BLOCK_37 | HuVrdQtttozQVlx1Pp2cwKmjnJh -->
**Q: 知识规则在什么时候被检测？我如何知道是否生效？**

<!-- END_BLOCK_37 -->
<!-- BLOCK_38 | TKgYdVPzco8XwQxGW4yc6QVknKe -->
**A:** 知识的冲突、重复等检测主要发生在**创建和编辑保存时**。如果检测失败，你会在页面上收到明确的失败原因提示。任务执行时，Aime 会根据 `use_when` 场景自动匹配并应用相关规则。你可以在任务结果详情页的 Aime 执行过程中，查看“本次命中的知识/规则”信息，确认规则是否已按预期生效。

<!-- END_BLOCK_38 -->
<!-- BLOCK_39 | VB5PdcMDLotLQCxWBSucuILunyg -->
![图片](img_CGTQbPO2WoPdD9x0uZFczHX8nVb.png)

<!-- END_BLOCK_39 -->
<!-- BLOCK_40 | B8fAd6cKkoupJ3xQcwTcvtufn8e -->


<!-- END_BLOCK_40 -->
<!-- BLOCK_41 | XqmwdQ1XdoTcokxBd2DcW8UAnrh -->
**Q: 我更新了文档库里的飞书文档，Aime 会立刻知道吗？**

<!-- END_BLOCK_41 -->
<!-- BLOCK_42 | R1dmd5ERgoOvJIxpU1LcCC1Inyq -->
**A:** 不会立刻知道。文档库的同步有一定延迟（默认检测文档的更新情况自动更新以保持同步）。如果你的文档内容有重要更新，并希望立即在 Aime 任务中生效，建议进入 **资源配置** -> **文档库 / 知识配置**，找到对应的文档，并点击 **手动更新** 按钮。

<!-- END_BLOCK_42 -->
<!-- BLOCK_43 | MChRdPTcXo1wlhxn7gAcaoponVd -->


<!-- END_BLOCK_43 -->
<!-- BLOCK_44 | VPr0ddqs3ovHtmxqIBZcD1ROnVc -->
**Q：我想要录入多条知识，但是现在每个空间有 20 条空间内公开和 10 条个人可见知识的数量限制。在有多条具有层级结构的知识期望录入的场景下我应该如何录入知识？**

<!-- END_BLOCK_44 -->
<!-- BLOCK_45 | CMccduPd5ojhMfxHMfhcdN7Knmh -->
A：目前有两种方式可以按需尝试。
方案一：可以使用飞书文档作为主目录索引来承载具有层级的多条知识。详情 & 示例可参考：[Aime 知识：使用飞书文档分层管理知识](https://bytedance.larkoffice.com/wiki/GgNlw49KmiJ7uCkcDnWcY79OnSf)
方案二：通过 skill.zip 形式上传结构化的知识文件信息，详细可参考：[Aime Skill 指南](https://bytedance.larkoffice.com/wiki/BSVVwNRRdi6TDSkTHJNcUDiznbe)

<!-- END_BLOCK_45 -->
<!-- BLOCK_46 | Lf60dX8TSomE59xyjyYc1X4AnLg -->


<!-- END_BLOCK_46 -->
<!-- BLOCK_47 | C9fcdJa3howYbYxrahccvnzmnJf -->
**Q: 为什么我和同事在同一个项目空间，使用同一个任务指令，但 Aime 检索到的代码或文档内容不同？**

<!-- END_BLOCK_47 -->
<!-- BLOCK_48 | GQfud8aSooRUMexpSCMcIv6MnXg -->
**A:** 这是因为 Aime 在访问部分资源（如代码仓库、TCE 服务、链接形式的飞书文档）时，会模拟**当前操作者**的身份进行访问，并遵守其个人权限。如果你的同事没有某个代码仓库的 `clone` 权限，那么即使该仓库已在资源中配置，他在执行任务时也无法读取其中的内容。

<!-- END_BLOCK_48 -->
<!-- BLOCK_49 | UI7Udt3dqonKX5xi45qcPQalnzh -->


<!-- END_BLOCK_49 -->
<!-- BLOCK_50 | ZcITdyiDDoaTSixRKzacNNfgnGh -->
**Q: 文档库和知识配置里的“引用云文档”有什么区别？**

<!-- END_BLOCK_50 -->
<!-- BLOCK_51 | OTZDdJJ0Wowg62xpxMGcSuLHnwf -->
**A:** **文档库**是**被动检索**的背景信息源，Aime 会根据任务语义去“搜索”相关内容，适合存放大量、分散的参考资料（如团队 Wiki）。而**知识配置**中的“引用云文档”是**主动应用**的指导规则，具有最高优先级，只要触发条件满足，Aime 就会“遵循”其内容，适合存放必须严格遵守的规范和流程（如“发布流程手册”）。

<!-- END_BLOCK_51 -->
<!-- BLOCK_52 | WZgWdQSwio7b1sxQHiocIl5fnog -->


<!-- END_BLOCK_52 -->
<!-- BLOCK_53 | M9wfdvXkfovFMDxHvMycsfi6n0f -->
**Q: 多条知识很相似时如何处理？**

<!-- END_BLOCK_53 -->
<!-- BLOCK_54 | EJ7kdGMAloKwTPxKAGQcTaGfnKf -->
**A:** 录入时明确每条知识的使用时机， 尽量不要重合，不要模糊表述。可依据“使用时机边界、受众/范围、输入输出差异”进行拆分与去重；同时，考虑到知识的数量限制，建议可将跨场景公共步骤抽为一条“基础知识”供复用

<!-- END_BLOCK_54 -->
<!-- BLOCK_55 | MD9sdZUj1oqEsKxeC6ecDTFGnPh -->


<!-- END_BLOCK_55 -->
<!-- BLOCK_56 | FWtAd4LICoByl3xGuvBcW9pznad -->
## 附录
<!-- END_BLOCK_56 -->
<!-- BLOCK_57 | L12JdzNcHoT1pGxM5wQcJYvYnuf -->
### 资源配置字段总览
<!-- END_BLOCK_57 -->
<!-- BLOCK_58 | LheCd5ztvodwTAxJ6GBcWq8VnRA -->
<table header-row="true" col-widths="102,239,479">
    <tr>
        <td>资源类型</td>
        <td>主要配置字段</td>
        <td>格式要求/示例</td>
    </tr>
    <tr>
        <td>代码仓库</td>
        <td>Git 仓库地址</td>
        <td>`https://git.bytedance.net/group/repo.git`</td>
    </tr>
    <tr>
        <td>TCE 服务</td>
        <td>PSM (Product, Service, Module)</td>
        <td>`P.S.M.example-service`</td>
    </tr>
    <tr>
        <td>Meego</td>
        <td>Meego 空间或工作项 URL</td>
        <td>`https://meego.larkoffice.com/space/home/xxx`</td>
    </tr>
    <tr>
        <td>测试用例</td>
        <td>Bits 测试用例库空间地址</td>
        <td>`https://bits.bytedance.net/space/12345`</td>
    </tr>
    <tr>
        <td>文档库</td>
        <td>飞书文档/表格/Wiki 链接或文件上传</td>
        <td>`https://bytedance.larkoffice.com/wiki/xxxxxxxx`</td>
    </tr>
</table>

<!-- END_BLOCK_58 -->
<!-- BLOCK_59 | P1fPdD7nWo0TCNxaehucTIRbnOb -->


<!-- END_BLOCK_59 -->
<!-- BLOCK_60 | X6okdzkfYo4c4bxsPVCcCmFgnud -->
## 问题反馈
<!-- END_BLOCK_60 -->
<!-- BLOCK_61 | XRYHdQSNuoG4Ifx0QukcuzphnCd -->
如果你在配置或使用空间/空间自定义知识的过程中遇到任何问题，或有宝贵的优化建议，欢迎通过以下方式联系我们：

<!-- END_BLOCK_61 -->
<!-- BLOCK_62 | Wk98dKCENo06Yuxxe5Jc2Htonlb -->
<grid cols="2">
<column width="40">
  - **用户群**：[用户交流2群](https://applink.larkoffice.com/client/chat/chatter/add_by_link?link_token=a58qbbf6-b1e7-445f-8ca1-db2c5ed16b37)
</column>
<column width="60">
  - **联系我们**：你也可以直接联系空间管理员或@(lanjunjian@bytedance.com)@(dingdegao@bytedance.com)@(wangyiyun.0423@bytedance.com)
</column>
</grid>

<!-- END_BLOCK_62 -->
<!-- BLOCK_63 | HsGndPF9woW5HwxKBJlc9fKinUs -->


<!-- END_BLOCK_63 -->

</content>
