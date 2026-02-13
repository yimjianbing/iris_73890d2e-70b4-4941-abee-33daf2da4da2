"""
# `mcp:仓库说_23_search_nodes`

执行语义化的代码搜索。此工具允许用户使用自然语言（例如：'鉴权中间件在哪里'）在 repo_names 指定的一个或多个代码仓库中进行查询。如果你知道代码片段所在的 package 的话可以指定 package id，package_id 的构造方式为 [ModPath]?<PkgPath>。如果不知道可以不指定。

---

**Parameters Schema:**

{"type":"object","properties":{"package_ids":{"type":"array","description":"the package ids","properties":{},"items":{"type":"string","description":"the identity of package, in format of [ModPath]?\u003cPkgPath\u003e. (NOTICE: the PkgPath must be full package path)","properties":{}}},"question":{"type":"string","description":"natural language description","properties":{}},"repo_names":{"type":"array","description":"the repo names","properties":{},"items":{"type":"string","properties":{}}}},"required":["question","repo_names"]}

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
            tool_name="mcp:仓库说_23_search_nodes",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
