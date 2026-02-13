"""
# `mcp:SlardarApp_get_alog_by_url`

根据 slardar alog 页面链接获取 alog 日志数据

---

**Parameters Schema:**

{"type":"object","properties":{"alog_slardar_link":{"type":"string","description":"slardar alog 页面链接","properties":{}}},"required":["alog_slardar_link"]}

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
            tool_name="mcp:SlardarApp_get_alog_by_url",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
