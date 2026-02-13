"""
# `mcp:a_map_maps_ip_location`

IP 定位根据用户输入的 IP 地址，定位 IP 的所在位置

---

**Parameters Schema:**

{"type":"object","properties":{"ip":{"type":"string","description":"IP地址","properties":{}}},"required":["ip"]}

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
            toolset="a_map",
            tool_name="mcp:a_map_maps_ip_location",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
