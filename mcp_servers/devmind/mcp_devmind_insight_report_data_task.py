"""
# `mcp:devmind_insight_report_data_task`

Query task info for a specific insight report, including user's customized prompt and data info about how to analyze this task

---

**Parameters Schema:**

{"type":"object","properties":{"execute_id":{"type":"string","description":"The ID of task to execute","properties":{}}},"required":["execute_id"]}

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
            tool_name="mcp:devmind_insight_report_data_task",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
