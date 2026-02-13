"""
# `mcp:SlardarWeb_get_perf_page_overview_by_link`

通过链接获取上报到 Slardar 上页面整体的性能指标，支持长链接和短链接

---

**Parameters Schema:**

{"type":"object","properties":{"link":{"type":"string","description":"Slardar 性能总览的链接（支持长链接和短链接）","properties":{}}},"required":["link"]}

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
            toolset="SlardarWeb",
            tool_name="mcp:SlardarWeb_get_perf_page_overview_by_link",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
