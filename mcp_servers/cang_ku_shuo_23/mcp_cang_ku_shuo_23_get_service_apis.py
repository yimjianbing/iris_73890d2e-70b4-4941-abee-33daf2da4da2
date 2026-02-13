"""
# `mcp:仓库说_23_get_service_apis`

获取指定仓库API接口的功能描述、处理流程及参数信息

---

**Parameters Schema:**

{"type":"object","properties":{"api_names":{"type":"array","description":"the api name","properties":{},"items":{"type":"string","properties":{}}},"repo_name":{"type":"string","description":"the repo name","properties":{}}},"required":["repo_name","api_names"]}

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
            tool_name="mcp:仓库说_23_get_service_apis",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
