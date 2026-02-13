"""
# `mcp:仓库说_23_get_packages_detail`

精确获取指定包（package）的 功能、流程 及 包内的文件列表

---

**Parameters Schema:**

{"type":"object","properties":{"package_ids":{"type":"array","description":"the package identities","properties":{},"items":{"type":"string","description":"the identity of package, in format of [ModPath]?\u003cPkgPath\u003e. (NOTICE: the PkgPath must be full package path)","properties":{}}},"repo_name":{"type":"string","description":"the repository name","properties":{}}},"required":["repo_name","package_ids"]}

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
            toolset="仓库说_23",
            tool_name="mcp:仓库说_23_get_packages_detail",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
