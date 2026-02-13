"""
# `mcp:SlardarApp_autofix_get_harmony_issue_main_log`

根据用户提供的Harmony应用Slardar issue链接，获取这个issue的关键信息，崩溃线程调用栈、异常类型、崩溃原因、崩溃附带参数、关键栈帧git信息

---

**Parameters Schema:**

{"type":"object","properties":{"slardar_link":{"type":"string","description":"Slardar issue详情页链接","properties":{}}},"required":["slardar_link"]}

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
            tool_name="mcp:SlardarApp_autofix_get_harmony_issue_main_log",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
