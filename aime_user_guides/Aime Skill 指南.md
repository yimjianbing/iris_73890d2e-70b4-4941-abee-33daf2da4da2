<title>Aime Skill 指南</title>
<url>https://bytedance.larkoffice.com/wiki/BSVVwNRRdi6TDSkTHJNcUDiznbe</url>
<content>
<callout icon="pushpin" bgc="4" bc="4">
Aime Skill 体系完全兼容 Claude Skill，正在探索增强 SKILL
Skill 的本质：是一个专业/私有领域的小型模型知识/技能库，通过 Skill 建设可以基于 Aime 探索更多适配业务场景的玩法。期待与你共同探索 Skill 的最佳实践！
</callout>

# 使用指南
<callout icon="soccer" bgc="2" bc="2">
Skill 核心优势：
- 按需加载，不过多占用上下文
- 支持脚本，资源固定下来，提升效率，提升稳定性
</callout>

<table header-row="true" col-widths="218,237,366">
    <tr>
        <td>配置入口</td>
        <td>字段说明与要求</td>
        <td>最佳实践或说明</td>
    </tr>
    <tr>
        <td>![图片](img_VRF4b8CvfoSlfKxx6etct1iInhf.png)
![图片](img_DeI3bXRcToIEM5xT5mRcPO6tnjp.png)
![图片](img_ZHfobEbYYoWJjjxzYVgcJD3Hn4c.png)</td>
        <td>仅支持 zip 上传，zip 必须符合 skill 标准：
- 包含 SKILL.md，并且SKILL.md 里面只能包含 name 和 description的表头
例子：
![图片](img_K2WIbsykXo9m8bxqUaDcN80Mn4c.png)
要求：
- `SKILL.md` 主体内容应保持简洁，通常低于 5k tokens
- `name` 最多 64 个字符
- `description` 最多 1024 个字符，不能包含 XML 标签， 应说明该技能（Skill）的功能的和使用场景</td>
        <td>按官方的最佳实践要求进行即可
推荐参考官方文档：
英文版本：https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices
中文版本：https://platform.claude.com/docs/zh-CN/agents-and-tools/agent-skills/best-practices
Skill 示例，Github 仓库： https://github.com/anthropics/skills
Skill Market（可自行浏览下载所需的 skill 文件）：
http://skillsmp.com/
https://skills.sh/


- 快捷开发使用 aime-skill： [Aime Skill Creator 使用指南](https://bytedance.larkoffice.com/wiki/WK8Vwt2fiiKwTQkGVvZcGoIen8f)
- 详细skill 开发指南，参考：[Aime Skill 开发指南](https://bytedance.larkoffice.com/wiki/MQAnwMcdFiFKrAkCIKQcUTPon8b)
- 内置skill使用指南： [Aime 官方内置skill](https://bytedance.larkoffice.com/wiki/UkoYwgS7siEFolkPnB4cW8e3nSc)
- Skill 加载mcp： [Aime Skill MCP 配置指南](https://bytedance.larkoffice.com/wiki/FJj7wHMAMiH2IekOWxYcezkMnmd)</td>
    </tr>
</table>

如果你不想用 gui 上传，可以使用 CLI 直接上传，[Aime Skill CLI 快速上手指南](https://bytedance.larkoffice.com/wiki/UlgSwWSORiI0cFkqCcPcQ9GDnBc)

# 推荐的使用场景
<table header-row="true" col-widths="115,150,348,378">
    <tr>
        <td>场景</td>
        <td>说明</td>
        <td>例子</td>
        <td>Skill 例子</td>
    </tr>
    <tr>
        <td>高优先级的知识分级，效果提升</td>
        <td>借助按需加载特性，知识的召回，效果优于纯 RAG 召回，也优于纯 Agentic 的方式。</td>
        <td>目前客户端，前端，服务端有很多组件的使用文档，内容都很多，现在的知识召回大多依赖 RAG 的形式召回切片，效果不太好，借助 Skill 按需加载召回，效果提升。
**不建议将全量业务知识库全部注入 Skill！请人工筛选后，配置最高优先级的业务背景或规则**
<grid cols="2">
<column width="84">
  ![图片](img_UoX8bGW2foxPWrxazMlcXC7mnkf.png)
</column>
<column width="15">
  ![图片](img_BQwIbn9hfo1FZ9xciIuc0byZn5g.png)
</column>
</grid></td>
        <td>![文件](file_file_assem-android_1.zip)</td>
    </tr>
    <tr>
        <td>接入本地工具</td>
        <td>目前 Aime 不支持local mcp 用户接入，只能访问远程资源，如 mcp，接口访问。 比如需要对代码实时 lint 检测，访问本地资源的 mcp，aime 用户是无法直接接入local mcp的</td>
        <td>可以把固化的脚本，文件集成 Skill ，如下 SKILL.md 内容
```json
xxx功能：  
使用场景：xxxx  
调用 `python script/xxx.py`     
  
xxx功能：  
使用场景：xxxx  
调用 `python script/xxx.py`     
  
xxx功能：  
使用场景：xxxx  
调用 `python script/xxx.py`
```</td>
        <td>由于前面tool涉及保密信息，这里举例一个 apktool的例子
![文件](file_file_apktool-linux-download_apktool-linux-skill_1.zip)</td>
    </tr>
    <tr>
        <td>复杂场景的mcp</td>
        <td>mcp工具超过20个，模型世界知识不足以很好的使用你提供的mcp工具时</td>
        <td>​-</td>
        <td>​-</td>
    </tr>
    <tr>
        <td>workflow 场景，如 1024活动</td>
        <td>固定每次生成的网页稳定，提升执行速度</td>
        <td>SKILL 核心内容
![图片](img_WTZjbKRFmo0Pl9xBBUgcI5Bynnd.png)</td>
        <td>![文件](file_file_aime-annual-report-1024-skill_1.zip)

![图片](img_PxZ3bfWFfohdlDxCmNQcUnjTnVc.png)</td>
    </tr>
</table>

# Skill 热点 FAQ
## Skill 和 Aime 模版的关系
Skill 和 模版其实没有直接的对比关系，由于aime 存在模版的概念，这里说明一下（仅说明 Skill 当 sop的情况）

- Skill：是小的sop，也可以当大的 sop 使用，模型主动召回使用，由 prompt 控制使用

- SOP模版：一个任务完整的流程全部固定下来，执行更稳定

所以推荐方式：

- 如果你的任务只需要完成一部分 SOP的能力，则推荐使用Skill

- 如果你的任务需要全部固化，推荐使用模版。 当然为了更稳定，推荐**模版 + Skill&nbsp;**的组合方式

## Skill 与 MCP 的关系对比，如何抉择？
Claude 官方说明：https://claude.com/blog/extending-claude-capabilities-with-skills-mcp-servers

连接了多个 MCP 时，模型会在每一轮对话中都尝试把这些工具的元数据全部塞进上下文，这会导致 Token 消耗极快，且容易干扰模型注意力。**跟单独配置 MCP 相比，Skills 会通过动态加载很好的解决 MCP 占用过多上下文的问题**：首先只会看到 Skills 的描述/description。只有当模型判断当前任务确实需要该功能时，才会实时加载对应的 MCP 工具定义。



以下是 Aime 实践心得（仅供参考）

<table header-row="true" col-widths="100,226,242,252">
    <tr>
        <td>分类</td>
        <td>优势</td>
        <td>劣势</td>
        <td>推荐使用场景</td>
    </tr>
    <tr>
        <td>mcp</td>
        <td>- 直接注册到模型，方便快捷调用，稳定性高</td>
        <td>- 当工具很多时，注册给模型成了一种负担
- 当是一个复杂 mcp ，或者模型的世界知识不认识时，无法在工具的描述中很好地教会mcp应该如何使用</td>
        <td>当mcp很简单时，比如工具很少，或者模型的世界知识大概知道这个mcp应该如何使用时，mcp合适</td>
    </tr>
    <tr>
        <td>skill</td>
        <td>- 等于配备知识，配置最佳实践的增强版mcp（与mcp对比场景，当然他也可以只当做知识）
- 按需加载，是他核心优势，当工具很多时也能正常work</td>
        <td>- 有一次工具调用效率损耗
- 如果简单场景，作为原子调用，稳定性低于mcp</td>
        <td>当mcp很复杂时，工具很多时，需要配备使用方式时。优先推荐他。就算有效率损失，他也是最佳实践方式</td>
    </tr>
</table>

- 如果新写功能，按上面使用场景选择就好

- 如果对于存量，简单场景，保留mcp，复杂场景推荐skill 

> 很快 aime 会出复杂 mcp 转 skill 的最佳实践
> 



# Aime Skill 友情链接
<grid cols="2">
<column width="50">
  ![图片](img_OAwMbH7ewohK5oxBoHmcuh3Nnjc.png)
</column>
<column width="50">
  - 快捷开发使用 aime-skill-creator： [Aime Skill Creator 使用指南](https://bytedance.larkoffice.com/wiki/WK8Vwt2fiiKwTQkGVvZcGoIen8f)
  - 详细原理指南，参考：[Aime Skill 开发指南](https://bytedance.larkoffice.com/wiki/MQAnwMcdFiFKrAkCIKQcUTPon8b)
  - 内置skill使用指南： [Aime 官方内置skill](https://bytedance.larkoffice.com/wiki/UkoYwgS7siEFolkPnB4cW8e3nSc)
</column>
</grid>



# English Version: [Aime Skill Guide](https://bytedance.larkoffice.com/docx/WvTVdtB5LomI5JxbhYRc5cTInOe)

</content>
