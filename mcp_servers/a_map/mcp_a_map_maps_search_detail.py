"""
# `mcp:a_map_maps_search_detail`

查询关键词搜或者周边搜获取到的POI ID的详细信息

---

**Parameters Schema:**

{"type":"object","properties":{"id":{"type":"string","description":"关键词搜或者周边搜获取到的POI ID","properties":{}}},"required":["id"]}

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
            tool_name="mcp:a_map_maps_search_detail",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
