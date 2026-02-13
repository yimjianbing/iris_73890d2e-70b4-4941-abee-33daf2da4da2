"""
# `mcp:仓库说_23_infra_search`

获取字节跳动（公司）内部基础设施和基础组件的用法，具体用法如下：填写 Question 为要搜索的问题。当涉及到公司内部（字节跳动内部）组件、基础设施、框架等相关内容时优先使用该工具查询。字节跳动基础组件包括 Golang HTTP 框架 Hertz、RPC 框架 Kitex、Redis、MySQL 等。提问方式应为 ${component} + ${用法} 的方式提问，如：Hertz 反向代理如何使用。注意不能**组合使用**，如Hertz中如何使用MySQL是不正确的。

---

**Parameters Schema:**

{"type":"object","properties":{"component":{"type":"string","description":"组件","properties":{},"format":""},"question":{"type":"string","description":"查询问题","properties":{},"format":""}}}

"""
import os
import sys
import site
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    payload_json = " ".join(sys.argv[1:])
    try:
        result = call_aime_tool(
            toolset="仓库说_23",
            tool_name="mcp:仓库说_23_infra_search",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
