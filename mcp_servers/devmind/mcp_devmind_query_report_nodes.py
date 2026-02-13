"""
# `mcp:devmind_query_report_nodes`

Query the list of reporting line nodes related to the user

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
            toolset="devmind",
            tool_name="mcp:devmind_query_report_nodes",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
