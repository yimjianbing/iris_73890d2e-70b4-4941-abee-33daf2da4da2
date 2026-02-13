"""
# `mcp:devmind_manage_favorite`

Create or delete a favorite metric

---

**Parameters Schema:**

{"type":"object","properties":{"status":{"type":"string","description":"Status: '1' to create, '0' to delete","properties":{}},"story_id":{"type":"string","description":"The ID of the story metric to manage","properties":{}}},"required":["story_id","status"]}

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
            tool_name="mcp:devmind_manage_favorite",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
