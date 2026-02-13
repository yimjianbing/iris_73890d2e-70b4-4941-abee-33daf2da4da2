"""
# `mcp:lark_sheets_update_lark_init_sheet_headers`

Insert first row or column or both, then batch update headers from source xlsx

---

**Parameters Schema:**

{"type":"object","properties":{"dimension":{"type":"string","description":"必填，ROWS/COLUMNS/BOTH","properties":{}},"document_url":{"type":"string","description":"必填，飞书表格链接","properties":{}},"sheet_name":{"type":"string","description":"必填，工作表名称","properties":{}},"source_file_path":{"type":"string","description":"必填，源xlsx文件绝对路径","properties":{}}},"required":["document_url","sheet_name","dimension","source_file_path"]}

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
            toolset="lark_sheets_update",
            tool_name="mcp:lark_sheets_update_lark_init_sheet_headers",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
