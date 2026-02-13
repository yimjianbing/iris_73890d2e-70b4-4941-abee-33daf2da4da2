"""
# `mcp:SlardarApp_get_crash_issue_list`

根据用户提供的Slardar列表页的链接和count个数，获取列表页的issue列表

---

**Parameters Schema:**

{"type":"object","properties":{"count":{"type":"integer","description":"issue的个数","properties":{}},"is_complete":{"type":"boolean","description":"是否返回完整数据，默认返回精简后的数据","properties":{}},"slardar_link":{"type":"string","description":"Slardar 列表页链接","properties":{}}},"required":["slardar_link"]}

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
            tool_name="mcp:SlardarApp_get_crash_issue_list",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
