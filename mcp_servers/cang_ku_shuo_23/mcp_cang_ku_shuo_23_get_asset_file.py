"""
# `mcp:仓库说_23_get_asset_file`

获取仓库内的 asset，包括 readme、idl 文件、配置文件等。如果你传递的文件不存在，我会返回所有可获取的文件，你可以从中找到需要的。注意，这个工具不会返回代码文件，如需获取代码文件使用工具 get_files_detail

---

**Parameters Schema:**

{"type":"object","properties":{"file_paths":{"type":"array","description":"文件路径列表","properties":{},"items":{"type":"string","properties":{},"format":""},"format":""},"repo_name":{"type":"string","description":"仓库名","properties":{},"format":""}}}

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
            tool_name="mcp:仓库说_23_get_asset_file",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
