"""
# `mcp:Bits-AppCenter_get_app_info`

用于获取应用中心的应用信息详情，应用中包含IAC SOT文件的仓库信息，以及应用的包含的组件信息

---

**Parameters Schema:**

{"type":"object","properties":{"appcenter_app_id":{"type":"string","description":"id of this APP","properties":{}}},"required":["appcenter_app_id"]}

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
            tool_name="mcp:Bits-AppCenter_get_app_info",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
