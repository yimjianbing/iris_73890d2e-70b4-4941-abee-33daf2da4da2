"""
# `mcp:lark_create_lark_doc`

Create a Lark document based on a Markdown file (.lark.md), whenever possible, prioritize using .lark.md files, the .lark.md file content must strictly follow Feishu/lark specific rules, as list in Lark Markdown Formatting. Do not call this tool multiple times in a single task. Must Use pwd && ls to confirm the file path before use. This will return a Lark/Feishu link, they are the actual final Lark/Feishu documents. There is no need to further verify them.

---

**Parameters Schema:**

{"type":"object","properties":{"file_path":{"type":"string","description":"必填，文件绝对路径，支持 Markdown文件（.lark.md），比如：/workspace/iris_e7c707a5-ae78-42d0-b045-1882a9f0a4d7/demo.lark.md，注意：1. 禁止填url 2. 文件路径必须真实存在（必须提前使用 pwd \u0026\u0026 ls 确认文件路径） 3. 尽量优先使用 .lark.md 文件，文件内容必须遵循 Feishu/lark specific rules, as list in Lark Markdown Formatting","properties":{}},"title":{"type":"string","description":"必填，文档标题。注意：1. 标题中务必不要包含用户的名字 2. 标题避免冗长 3. 在标题中减少使用括号、冒号等，最多使用一次 4. 标题中不要包含额外说明","properties":{}}},"required":["file_path","title"]}

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
            toolset="lark",
            tool_name="mcp:lark_create_lark_doc",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
