"""
# `mcp:SlardarApp_alog_event_fetch`

根据 aid 和 os 获取 alog 自定义事件

---

**Parameters Schema:**

{"type":"object","properties":{"aid":{"type":"number","description":"应用 ID","properties":{}},"os":{"type":"string","description":" 操作系统类型","properties":{}}}}

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
            toolset="SlardarApp",
            tool_name="mcp:SlardarApp_alog_event_fetch",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
