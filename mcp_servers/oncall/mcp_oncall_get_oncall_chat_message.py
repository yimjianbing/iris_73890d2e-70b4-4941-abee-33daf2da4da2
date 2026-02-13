"""
# `mcp:oncall_get_oncall_chat_message`

根据oncall ID查询群聊

---

**Parameters Schema:**

{"type":"object","properties":{"id":{"type":"string","description":"oncall id，此处填写oncall id","properties":{}}},"required":["id"]}

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
            toolset="oncall",
            tool_name="mcp:oncall_get_oncall_chat_message",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
