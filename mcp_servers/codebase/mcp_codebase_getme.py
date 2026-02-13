"""
# `mcp:codebase_GetMe`

Get my self (an authenticated Codebase user or an application).
It returns the information of myself. Consider to use this when a request include "me", "my", "我".

---

**Parameters Schema:**

{"type":"object","properties":{"Reason":{"type":"string","description":"Optional. Reason the session was created.","properties":{}}}}

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
            toolset="codebase",
            tool_name="mcp:codebase_GetMe",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
