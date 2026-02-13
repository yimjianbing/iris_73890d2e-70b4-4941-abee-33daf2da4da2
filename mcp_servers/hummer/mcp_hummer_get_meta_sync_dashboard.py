"""
# `mcp:hummer_get_meta_sync_dashboard`

查询一段时间内的Meta Sync总次数和平均耗时，耗时单位为毫秒

---

**Parameters Schema:**

{"type":"object","properties":{"appId":{"type":"string","description":"查询应用的AppId","properties":{}},"endDate":{"type":"string","description":"查询的终止日期，格式为YYYY-MM-DD","properties":{}},"packageName":{"type":"string","description":"查询应用的packageName","properties":{}},"startDate":{"type":"string","description":"查询的起始日期，格式为YYYY-MM-DD","properties":{}}},"required":["appId","packageName","startDate","endDate"]}

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
            tool_name="mcp:hummer_get_meta_sync_dashboard",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
