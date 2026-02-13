"""
# `mcp:devmind_write_task_result`

Write result to task instance

---

**Parameters Schema:**

{"type":"object","properties":{"result":{"type":"string","description":"The result to write","properties":{}},"task_instance_id":{"type":"string","description":"The ID of task to write","properties":{}}},"required":["task_instance_id","result"]}

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
            tool_name="mcp:devmind_write_task_result",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
