"""
# `mcp:hummer_get_build_detail_with_url`

根据 hummer 链接获取构建信息，包括appId，packageName，工程名称，用户email，提交CID，开始时间，variantName，模块数量，总耗时，configuration耗时，task耗时，是否增量，buildType，错误堆栈

---

**Parameters Schema:**

{"type":"object","properties":{"url":{"type":"string","description":"hummer 链接，例如：https://hummer.bytedance.net/singlebuild/overview?id=77550965","properties":{},"format":"uri"}},"required":["url"]}

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
            tool_name="mcp:hummer_get_build_detail_with_url",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
