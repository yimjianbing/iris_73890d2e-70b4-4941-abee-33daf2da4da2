"""
# `mcp:BAM API 文档_24_get_api_definition_info_with_endpoint_id`

Obtain the API definition information through endpointId. If you know endpointId, call this method first.

---

**Parameters Schema:**

{"type":"object","properties":{"branch":{"type":"string","description":"branch represents the branch of the API interface, which comes from the branch field entered by the user. ","properties":{}},"endpointId":{"type":"string","description":"endpoint id represents the method id of the API, which comes from the endpointId field entered by the user","properties":{}},"version":{"type":"string","description":"version represents the version of the API interface, which comes from the version field entered by the user. And Version example: 1.0.21. ","properties":{}}},"required":["endpointId"]}

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
            tool_name="mcp:BAM API 文档_24_get_api_definition_info_with_endpoint_id",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
