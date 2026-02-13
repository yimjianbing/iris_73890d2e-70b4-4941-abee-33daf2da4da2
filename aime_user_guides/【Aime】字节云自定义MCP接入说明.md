<title>【Aime】字节云自定义MCP接入说明</title>
<url>https://bytedance.larkoffice.com/wiki/MXrBwKE2FiL0c8k9xe8cQgQfnue</url>
<content>
<callout icon="camping" bgc="2" bc="2">
<font background_color="light_red">如果是</font>**<font background_color="light_red">字节云的MCP</font>**<font background_color="light_red">，推荐用字节SDK接入，没有鉴权烦恼，永久生效，任何人使用都不会被权限卡住。</font>

<font background_color="light_yellow">2026.1.5Update</font>：Aime 有CN和I18n控制面。<font background_color="light_yellow">由于公司网络隔离，CN只能访问CN MCP；I18n只能访问I18n MCP</font>（除非做了网络打标）。 
1. cn地址：https://aime.bytedance.net/chat

2. i18n地址: https://aime.tiktok-row.net/chat

</callout>

# 接入方式
<callout icon="trophy" bgc="2" bc="2">
此处的SSE和Streamable HTTP接入方式**适用所有实现了MCP协议的服务**，不是仅限字节云MCP。
</callout>

## SSE 接入方式
1. 获取SSE URL 

> 字节云 MCP Server 平台链接：https://cloud.bytedance.net/faas/mcp_servers?type=own&x-resource-account=public&x-bc-region-id=bytedance
> 

![图片](img_Ln5Ebo42doH39qxUlkXcCerYnHd.png)

## Streamable 接入方式
1. 如SSE 接入方式获取SSE URL

2. 将 SSE URL的 /sse 替换为 /mcp（或者直接贴到文档使用替换功能）


![图片](img_Y6aXbwiY0o9JH8x8HdpcSUtznFe.png)

1. 在AIME中新建自定义MCP，选择StreamableHTTP，将替换后链接填入下方的URL中

![图片](img_MMsJboB8AoLeYyxymcecvvBunSg.png)

## 字节云SDK 接入方式（推荐）
1. 获取字节云MCP 服务PSM 

![图片](img_CCjlb8Wszo5QXPxmyHpcdrwtnhd.png)

1. 如下图配置，配置个人MCP

![图片](img_JTnCbzNnLobDuix6Uh2c0TAgnfg.png)

PS：如果权限申请工单完成后还是通过不了校验。有可能是因为字节云MCP那边还没发布，操作下发布即可。

![图片](img_PUw1bCfzno63tPxZlrDc4n1vnvg.png)

# MCP更多说明
[Aime - 自定义MCP调试使用手册](https://bytedance.larkoffice.com/docx/Oz7edg6mlonTbIxqJjkc8TCTnqe)



# FAQ
<!-- 同步块开始（源文档: Oz7edg6mlonTbIxqJjkc8TCTnqe，源块: STMNdqH4PsBRRHbUofqcTr7Wnih）-->
### Q： MCP怎么调试PPE环境？
A：StreamableHTTP和SSE可以通过配置Header鉴权方式配置多环境参数，如图。但需要注意，如果你的MCP依赖x-jwt-token，需要自己显式填写对应KV。因为选了Header鉴权将不会再传递用户字节云Token到MCP。

![图片](img_WcelbXpl8ocFeWxCJL7cSMJSnTh.png)



### Q：为什么我的MCP请求不通？
A：有几种可能：

1. Aime 有CN和I18n控制面。2026.1.5Update：<font background_color="light_yellow">由于公司网络隔离，CN只能访问CN MCP；I18n只能访问I18n MCP</font>（除非做了网络打标）。 因为Aime在CN or I18n Prod，所以无法访问Boe、Devbox、I18n等地域的MCP服务。
	1. cn：https://aime.bytedance.net/chat
	2. i18n: https://aime.tiktok-row.net/chat

2. MCP的配置有问题，比如权限配置。请检查下是否有使用MCP服务的权限（大部分是字节云MCP，可以看看字节云平台上有没有对应MCP的调用权限）。注意：使用StreamHTTP方式接入，需要调用者自行到AI PaaS申请对应MCP的调用者权限。使用SDK方式接入的同学可以点击页面申请授权的给Aime授权，如果还是无效，可以参考2.1

3. 如果是<font background_color="light_red">I18N MCP </font>且使用HTTP or SSE配置。形如``https://xxxx.mcp.tiktok-row.net``。这是因为这是OG域名，需要替换成``https://xxxx.``mcp.byteintl.net````域名Aime才可以在生产网访问



### Q：为什么我本地能通，但是Aime i18n控制面添加MCP失败？
如果你使用的是Streamable HTTP或者SSE接入，请检查你的域名是否为生产网可访问的域名。办公网能使用的域名是OG域名，生产网不可以访问，需要使用生产网域名。 [ROW OG Oncall 自查文档](https://bytedance.larkoffice.com/docx/UD38dOZG3olQbbxdpyEclrRknMS)

![图片](img_YF2BbjLyuoMNSyxUUVvcFlVPnCd.png)



### Q：一直报调用失败 or JsonSchema校验失败
[Json Schema 校验失败案例](https://bytedance.larkoffice.com/wiki/SwgYwR5sRiAXzqkaxaQc8WajnXb)



### Q：MCP如何获取调用者的身份
Aime工具调用时默认会在请求的Header传递调用者的字节云token，key：x-jwt-token。**注意**：如果是用**字节云SDK且在字节云工具配置自定义**接入，由于字节云SDK限制，header信息被存储在body.params._mata.headers中，且为大小写敏感，Server端接收时可以参考下。

> 字节云token校验&解析官方文档[https://cloud.bytedance.net/docs/bytecloud/docs/63c4c6df7e9d2a021ec21002/6530ed91edc2c702f6a977cd?x-resource-account=public&x-bc-region-id=bytedance](https://cloud.bytedance.net/docs/bytecloud/docs/63c4c6df7e9d2a021ec21002/6530ed91edc2c702f6a977cd?x-resource-account=public&x-bc-region-id=bytedance)
> 

![图片](img_IaH6bYFvsocvrsxg8hXcaYXYnuh.png)



<!-- 同步块结束 -->


</content>
