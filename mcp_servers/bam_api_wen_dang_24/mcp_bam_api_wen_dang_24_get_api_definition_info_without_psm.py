"""
# `mcp:BAM API 文档_24_get_api_definition_info_without_psm`

API definition information can be obtained without entering psm parameters. This is a paging data. By default, the first 10 entries can be retrieved at most.

---

**Parameters Schema:**

{"type":"object","properties":{"branch":{"type":"string","description":"branch represents the branch of the API interface, which comes from the branch field entered by the user. ","properties":{}},"count":{"type":"string","description":"It represents the page size. If the user has not entered it, the default is 10. ","properties":{}},"ep_type":{"type":"string","description":"It represents the interface type and has only two values: http or rpc. ","properties":{}},"keyword":{"type":"string","description":"The keyword represents the method name or path of the API, which comes from the method/path field input by the user","properties":{}},"offset":{"type":"string","description":"It represents the page number. If the user does not enter it, it defaults to 0. ","properties":{}},"reqFilterKeys":{"type":"string","description":"Filter out the request schema-related fields based on filterKeys and do not return them to the user.If the user needs to filter multiple fields, use commas to connect multiple keys.","properties":{}},"respFilterKeys":{"type":"string","description":"Filter out the response schema-related fields based on filterKeys and do not return them to the user.If the user needs to filter multiple fields, use commas to connect multiple keys.","properties":{}},"version":{"type":"string","description":"version represents the version of the API interface, which comes from the version field entered by the user. And Version example: 1.0.21. ","properties":{}}},"required":["keyword"]}

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
            tool_name="mcp:BAM API 文档_24_get_api_definition_info_without_psm",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
