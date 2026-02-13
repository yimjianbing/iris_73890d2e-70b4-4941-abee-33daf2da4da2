"""
# `mcp:仓库说_23_get_repos_detail`

获取 指定仓库 详细信息，包括 仓库的概览、包（package）列表、服务API列表（仅对HTTP/RPC 服务类型有效）

---

**Parameters Schema:**

{"type":"object","properties":{"repo_names":{"type":"array","description":"the repository names","properties":{},"items":{"type":"string","properties":{}}}},"required":["repo_names"]}

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
            tool_name="mcp:仓库说_23_get_repos_detail",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
