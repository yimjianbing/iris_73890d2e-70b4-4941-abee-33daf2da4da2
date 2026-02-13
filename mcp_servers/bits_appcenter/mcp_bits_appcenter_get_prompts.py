"""
# `mcp:Bits-AppCenter_get_prompts`

应用相关的上下文信息，在进行任何相关操作之前都需要获取并遵守其中的提示词

---

**Parameters Schema:**

{"type":"object","properties":{}}

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
            toolset="Bits-AppCenter",
            tool_name="mcp:Bits-AppCenter_get_prompts",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
