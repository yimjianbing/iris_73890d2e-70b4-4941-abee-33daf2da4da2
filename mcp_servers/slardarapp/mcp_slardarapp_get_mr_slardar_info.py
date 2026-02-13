"""
# `mcp:SlardarApp_get_mr_slardar_info`

通过codebase project_id 和 iid 获取bits mr绑定的slardar信息和diff Patch

---

**Parameters Schema:**

{"type":"object","properties":{"iid":{"type":"integer","description":"codebase mr的id","properties":{}},"project_id":{"type":"integer","description":"codebase仓库的Id","properties":{}}},"required":["project_id","iid"]}

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
            toolset="SlardarApp",
            tool_name="mcp:SlardarApp_get_mr_slardar_info",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
