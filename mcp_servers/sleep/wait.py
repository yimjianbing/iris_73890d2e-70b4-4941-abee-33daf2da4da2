"""
# `wait`

This tool pauses execution for a specified number of seconds. Use this tool when the user explicitly asks to wait, delay, or pause for a certain amount of time before continuing with the next action.

---

**Parameters Schema:**

{"type":"object","properties":{"seconds":{"type":"number","description":"the number of seconds(float64) to wait","properties":{}}},"required":["seconds"]}

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
            toolset="sleep",
            tool_name="wait",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
