<title>Aime Skill 开发指南</title>
<url>https://bytedance.larkoffice.com/wiki/MQAnwMcdFiFKrAkCIKQcUTPon8b</url>
<content>
本地快速上传skill zip 使用cli 操作 [Aime Skill CLI 快速上手指南](https://bytedance.larkoffice.com/wiki/UlgSwWSORiI0cFkqCcPcQ9GDnBc)

# Skill  开发指南
## SKILL.md  Aime 实践心得
![图片](img_AGHlbk2GNoSVBCxAm9mcPv6pn4c.png)

**Name**

一个英文名称，遵循 Claude Skill 规范

**Description**

是什么，有什么能力，适用场景。 决定被模型主动召回的灵魂，需要写清楚

```yaml
---
name: feishu-card
description: <font color="purple">生成美观样式的飞书交互式消息卡片</font>，<font color="blue">支持通过邮箱、群组或webhook发送</font>。<font color="red">适用于创建公告、产品发布、系统通知、项目进度、日报、活动通知、庆祝祝贺或任何需要通过飞书分享的结构化内容</font>。
---
```

**具体内容 Content**

<callout icon="pushpin" bgc="4" bc="4">
核心原则： 按需加载，最小化原则
核心建议： 
- 如果是一个功能性 skill， 当模型看到你的 SKILL.md 时，就可以完成大多数任务了（70-80%的活），而不是依赖读取 references 才能干活，更复杂的活，才应该封装到 references 里面去完成。 这样能提升效率，节约 token。 所以 skill.md 的写法 <font color="red">很重要，很重要，</font>他是你这个 skill 的索引，指导干活的总纲。
- 如果模型已经知道的世界知识，不需要过多介绍，增加上下文占用。(**你认为他需要，其实他不需要**)
- 去除所有与该 skill 无关的描述，比如该接口由 xxx 实现，只要教会他怎么用 ，不需要教会他原理，引入无关描述（当然原理排查类的 skill 除外）
</callout>

举个例子： 比如你 skill 中有80个工具或者脚本，而常用的只有10个，那么 skill.md 的写法就应该如下，不止介绍工具，还需要介绍怎么使用，最佳实践

```markdown
<font background_color="light_green"># 工具介绍</font>
该Skill 主要通过以下工具去完成任务

## 工具1: xxx
```bash
python3 xxxx --prompt xxx --toolset xxx
```
参数说明：
- prompt 必需
- toolset 可选，使用值：files，bash 
....

## 工具10:xxx
xxx

<font background_color="light_green">## 更多工具</font>
如果你需要完成更多更复杂的任务，请参考 /references/tools.md，<font background_color="light_green">多数情况下不需要查看</font>


<font background_color="light_green"># 最佳实践</font>
xxx情况： 应该调用xx工具完成什么事情
xxx情况： 应该xxx完成什么事情

<font background_color="light_green">## 更复杂的实践</font>
如果你需要完成更多更复杂的任务，请参考 /references/best.md
```

## Skill-Creator 解读
目前官方的 Skill-Creator  对于要开发一个真正可用的 Skill 存在一些问题，如 Aime 实践心得的部分其实包含的不全。但是也有一些很好的思想值得开发者看看。

- 英文版本： https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md 

- 中文阶段： [Skill-Creator 中文解读](https://bytedance.larkoffice.com/wiki/EYE9wl0qZiLwuLkBurKcgiXWnMn)



## 如何在脚本中注入 jwt token
在 SKILL.md 中要求模型调用脚本时 <font background_color="light_green">设置 include_secrets=true </font>，然后使用环境变量获取  <font background_color="light_green">$AIME_USER_CLOUD_JWT</font>

```markdown
// SKILL.md
.....
```bash
python scripts/<你的脚本>.py
```
<font background_color="light_green">注意: 调用该脚本时，必须设置 include_secrets=true 以确保访问权限。</font>
.....
```

```python
## <你的脚本>
# 从环境变量获取JWT token
jwt_token = os.environ.get('AIME_USER_CLOUD_JWT')
   if not jwt_token:
       print("错误: 未找到环境变量 AIME_USER_CLOUD_JWT，请设置此环境变量后再试")
```

其他动态注入的环境变量列表

```go
***AimeEnvSessionID&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;***AimeShellEnviron = "AIME_SESSION_ID"
***AimeEnvSpaceID&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;***AimeShellEnviron = "AIME_SPACE_ID"
***AimeEnvCurrentUser&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;***AimeShellEnviron = "AIME_CURRENT_USER"
***AimeEnvCurrentUserEmail&nbsp;***AimeShellEnviron = "AIME_CURRENT_USER_EMAIL"
***AimeEnvUserCloudJWT&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;***AimeShellEnviron = "AIME_USER_CLOUD_JWT"
***AimeEnvUserCodeJWT&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;***AimeShellEnviron = "AIME_USER_CODE_JWT"

// 当前 workspace 所在路径
***IRIS_WORKSPACE_PATH&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;***AimeShellEnviron = "IRIS_WORKSPACE_PATH"
```

## 如何调用 Aime 内部 Tools
正在快速建设中，预计调用方式如下： 如果你有其他诉求，欢迎交流

```bash
curl -vv --location "$BASE_URL/tool/exec" \
--header "Content-Type: application/json" \
--data '{
    "name": "bash",
    "identifier": "terminal",
    "parameters": "{\"command\":\"ls -la\"}"
}'
```

## 动态上下文注入
<callout icon="construction" bgc="3" bc="3">
**即将上线** - 该功能近期才会上线，敬请期待！
</callout>

在 SKILL.md 中支持 `!`command` `语法，可以在 skill 内容发送给 AI 之前执行 shell 命令，将命令输出动态替换到占位符位置。这对于需要实时数据的场景非常有用。

**语法说明**

<table header-row="true" col-widths="350,350">
    <tr>
        <td>语法</td>
        <td>说明</td>
    </tr>
    <tr>
        <td>`!`command``</td>
        <td>执行命令，输出替换占位符</td>
    </tr>
    <tr>
        <td>`\!`command``</td>
        <td>转义，不执行命令</td>
    </tr>
</table>

**使用示例**

```markdown
---
name: pr-summary
description: 总结 PR 变更
---

## PR 上下文信息
- PR diff: !`gh pr diff`
- PR 评论: !`gh pr view --comments`
- 变更文件: !`gh pr diff --name-only`
- 当前时间: !`date`

## 你的任务
根据以上 PR 信息，总结这个 Pull Request 的主要变更...
```

**工作原理**

1. 当 Skill 被加载时，系统会扫描 SKILL.md 中的 `!`command`` 模式

2. 每条命令会在用户workspace下执行

3. 命令输出会替换原始占位符

4. AI 收到的是包含实际数据的完整内容

大输出处理

当命令输出超过 **8000 字符** 时，系统会自动：

1. 将输出保存到 `data/dynamic_output_{hash}.txt` 文件

2. 在原位置插入提示信息，指引 AI 读取该文件

```markdown
## 处理后效果（大输出场景）
- PR diff: 
[命令输出已保存到文件: data/dynamic_output_abc123.txt，请使用 read 工具读取该文件获取完整内容]
```

适用场景

- 获取 Git/GitHub 实时信息（PR、commit、branch 等）

- 注入当前时间、环境信息

- 读取动态配置或状态文件

- 任何需要实时数据的 Skill 场景



## Skill 中模型调用
- 目前如果 SKill 脚本中，想调用模型能力，建议自己申请 api_key，直接调用即可 
	- 方舟：https://cloud.bytedance.net/ark/region:ark+cn-beijing/overview
	- gpt 平台：https://gpt.bytedance.net/gpt_openapi/model-square
> 后续可以考虑脚本中直接调用 Aime 内部模型能力，目前安全和风险性还未设计，所以暂不支持
> 

# Aime 容器环境
- Python: 3.11.9   常见的依赖包不需要安装，如果自己的依赖包，需要安装

- Java: openjdk 17.0.6 2023-01-17

```markdown
SKILL.md 内容
步骤一，执行xxxx脚本，获取数据
步骤二，<font background_color="light_green">分析xxx的内容</font>（这个就是agent自己的模型能力）
步骤三，执行xxx脚本
xxxx
```

- Node v22.21.1    npm: 10.9.4

- Go version go1.24.9 linux/amd64

也可以自己在发起一个任务后，通过任意方式进入 webshell/ssh shell 去查看环境信息

<grid cols="2">
<column width="44">
  ![图片](img_XkMWbv4hWoSOR9xypfJc3CFVnfk.png)
</column>
<column width="55">
  ![图片](img_Udaqb8H7ootsQDxhzebcxGEzneh.png)
</column>
</grid>




</content>
