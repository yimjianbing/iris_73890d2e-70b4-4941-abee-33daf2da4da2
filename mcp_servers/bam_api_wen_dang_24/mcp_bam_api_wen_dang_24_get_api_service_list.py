"""
# `mcp:BAM API 文档_24_get_api_service_list`

Get a list of all api methods for a single PSM

---

**Parameters Schema:**

{"type":"object","properties":{"branch":{"type":"string","description":"branch represents the branch of the API interface, which comes from the branch field entered by the user","properties":{}},"psm":{"type":"string","description":"psm is a unique identifier, which comes from the psm entered by the user","properties":{}},"version":{"type":"string","description":"version represents the version of the API interface, which comes from the version field entered by the user","properties":{}}},"required":["psm"]}

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
            toolset="BAM API 文档_24",
            tool_name="mcp:BAM API 文档_24_get_api_service_list",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
