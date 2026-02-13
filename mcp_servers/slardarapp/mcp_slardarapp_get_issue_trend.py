"""
# `mcp:SlardarApp_get_issue_trend`

根据用户提供的Slardar issue链接，获取某个issue在一个时间段内的上报趋势

---

**Parameters Schema:**

{"type":"object","properties":{"end_timestamp":{"type":"integer","description":"结束时间戳","properties":{}},"issue_link":{"type":"string","description":"Slardar issue链接, 以https://slardar.bytedance.net/或者https://t.wtturl.cn开始的完整URL","properties":{}},"start_timestamp":{"type":"integer","description":"开始时间戳","properties":{}}},"required":["issue_link"]}

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
            tool_name="mcp:SlardarApp_get_issue_trend",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
