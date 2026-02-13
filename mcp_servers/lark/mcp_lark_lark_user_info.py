"""
# `mcp:lark_lark_user_info`

check the user info by user id, e.g for email zhangsan.001@bytedance.com, the 'zhangsan.001' is the user id

---

**Parameters Schema:**

{"type":"object","properties":{"user_id":{"type":"string","description":"required, lark user id, example: 12345678901234567890123456789012","properties":{}}},"required":["user_id"]}

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
            toolset="lark",
            tool_name="mcp:lark_lark_user_info",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
