"""
# `mcp:仓库说_23_get_files_detail`

获取指定路径文件的 ast 信息或配置文件、IDL 文件等。注意，你应该通过 get_repos_detail -> get_packages_detail -> get_files_detail 的路径去寻找文件，除非你明确知道文件名称。当你请求多个文件时，如果只要一个文件存在，就会返回该文件的信息。当所有文件不存在时，会返回所有的文件列表。

---

**Parameters Schema:**

{"type":"object","properties":{"file_path":{"type":"string","description":"the file path (relative to repo root)","properties":{}},"repo_name":{"type":"string","description":"the repo name","properties":{}}},"required":["repo_name","file_path"]}

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
            tool_name="mcp:仓库说_23_get_files_detail",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
