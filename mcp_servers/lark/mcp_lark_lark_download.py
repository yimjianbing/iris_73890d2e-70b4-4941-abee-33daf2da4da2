"""
# `mcp:lark_lark_download`

download file from the lark url, save locally, and return file path list, example: ["doc_title_xxx.lark.md", "sheet_title_xxx.xlsx"]

---

**Parameters Schema:**

{"type":"object","properties":{"document_url":{"type":"string","description":"required, lark document/sheet url, example: https://domain.larkoffice.com/docx/CCzFdEVGXoyLpmxxxxxx, https://bytedance.larkoffice.com/sheets/xxxxx?sheet=xxxxx","properties":{}}},"required":["document_url"]}

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
            tool_name="mcp:lark_lark_download",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
