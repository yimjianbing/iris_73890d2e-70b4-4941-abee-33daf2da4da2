"""
# `mcp:devmind_query_chart_info`

Query the chart info based on the chart url.

---

**Parameters Schema:**

{"type":"object","properties":{"chart_url":{"type":"string","description":"The chart url to query chart info, 不需要进行任何的转义，直接使用","properties":{}},"task_id":{"type":"string","description":"The task id to query chart info, 必填","properties":{}}},"required":["chart_url","task_id"]}

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
            toolset="devmind",
            tool_name="mcp:devmind_query_chart_info",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
