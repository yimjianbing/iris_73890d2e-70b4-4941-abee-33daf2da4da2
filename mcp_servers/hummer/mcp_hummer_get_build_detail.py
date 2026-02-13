"""
# `mcp:hummer_get_build_detail`

根据构建ID查询该次构建的详细信息，包括appId，packageName，工程名称，用户email，提交CID，开始时间，variantName，模块数量，总耗时，configuration耗时，task耗时，是否增量，buildType，错误堆栈

---

**Parameters Schema:**

{"type":"object","properties":{"id":{"type":"string","description":"构建ID","properties":{}}},"required":["id"]}

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
            toolset="hummer",
            tool_name="mcp:hummer_get_build_detail",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
