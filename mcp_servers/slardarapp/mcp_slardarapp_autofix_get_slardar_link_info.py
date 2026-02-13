"""
# `mcp:SlardarApp_autofix_get_slardar_link_info`

解析一个Slardar链接携带的信息，包括链接类型、携带参数（aid、os、crash_type等）、是否海外等

---

**Parameters Schema:**

{"type":"object","properties":{"link":{"type":"string","description":"Slardar链接","properties":{}}},"required":["link"]}

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
            tool_name="mcp:SlardarApp_autofix_get_slardar_link_info",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
