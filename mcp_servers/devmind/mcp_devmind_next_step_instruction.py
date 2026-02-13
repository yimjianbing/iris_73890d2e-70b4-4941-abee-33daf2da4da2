"""
# `mcp:devmind_next_step_instruction`

Query next step instruction for task

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
            tool_name="mcp:devmind_next_step_instruction",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
