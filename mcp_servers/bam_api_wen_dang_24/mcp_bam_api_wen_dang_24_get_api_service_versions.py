"""
# `mcp:BAM API 文档_24_get_api_service_versions`

Obtain the version list of a single PSM.

---

**Parameters Schema:**

{"type":"object","properties":{"branch":{"type":"string","description":"branch represents only obtaining the version list of this branch, which comes from the branch field entered by the user. Not filling it in indicates querying all interfaces.","properties":{}},"psm":{"type":"string","description":"psm is a unique identifier, which comes from the psm entered by the user","properties":{}}},"required":["psm"]}

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
            tool_name="mcp:BAM API 文档_24_get_api_service_versions",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
