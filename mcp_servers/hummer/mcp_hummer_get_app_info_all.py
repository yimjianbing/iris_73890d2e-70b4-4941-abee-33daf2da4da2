"""
# `mcp:hummer_get_app_info_all`

获取可查询的安卓应用信息，返回appId，appName，packageName

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
            toolset="hummer",
            tool_name="mcp:hummer_get_app_info_all",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
