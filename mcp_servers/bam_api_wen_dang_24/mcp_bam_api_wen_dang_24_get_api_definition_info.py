"""
# `mcp:BAM API 文档_24_get_api_definition_info`

Get API definition Info  through method and psm

---

**Parameters Schema:**

{"type":"object","properties":{"branch":{"type":"string","description":"branch represents the branch of the API interface, which comes from the branch field entered by the user","properties":{}},"method":{"type":"string","description":"method represents the method name of the API, which comes from the method field entered by the user","properties":{}},"psm":{"type":"string","description":"psm is a unique identifier, which comes from the psm entered by the user","properties":{}},"reqFilterKeys":{"type":"string","description":"Filter out the request schema-related fields based on filterKeys and do not return them to the user.If the user needs to filter multiple fields, use commas to connect multiple keys.","properties":{}},"respFilterKeys":{"type":"string","description":"Filter out the response schema-related fields based on filterKeys and do not return them to the user.If the user needs to filter multiple fields, use commas to connect multiple keys.","properties":{}},"version":{"type":"string","description":"version represents the version of the API interface, which comes from the version field entered by the user","properties":{}}},"required":["psm","method"]}

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
            tool_name="mcp:BAM API 文档_24_get_api_definition_info",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
