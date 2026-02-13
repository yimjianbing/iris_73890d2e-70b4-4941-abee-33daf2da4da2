"""
# `mcp:SlardarApp_get_sop_hook`

获取在SOP执行流程中关键节点的hook知识

---

**Parameters Schema:**

{"type":"object","properties":{"slardar_link":{"type":"string","description":"Slardar链接","properties":{}},"step":{"type":"string","description":"SOP执行的步骤","properties":{}}},"required":["slardar_link","step"]}

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
            tool_name="mcp:SlardarApp_get_sop_hook",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
