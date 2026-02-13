"""
# `mcp:BAM API 文档_24_get_api_doc`

Get API Doc Content

---

**Parameters Schema:**

{"type":"object","properties":{"directory":{"type":"string","description":"The directory for uploading api doc. It is recommended to use a complete repository name that includes the namespace path (usually in the format of 「owner/namespace/repo」 or 「owner/repo」), which can be achieved by parsing the URL of the Git remote repository.","properties":{}}},"required":["directory"]}

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
            tool_name="mcp:BAM API 文档_24_get_api_doc",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
