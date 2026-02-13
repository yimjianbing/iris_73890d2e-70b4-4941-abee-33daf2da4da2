"""
# `mcp:meego_get_work_item_metadata`

获取指定空间和工作项类型的必填字段列表，同时返回当前用户最近创建的同类型工作项历史记录（如果没有，则返回该空间内最近创建的同类型工作项）。返回内容包括：项目信息、工作项类型、必填字段列表（包含字段名称、类型、键值等）、历史工作项数据（及其来源说明）。

---

**Parameters Schema:**

{"type":"object","properties":{"simple_name":{"type":"string","description":"必填，空间名称","properties":{}},"work_item_type":{"type":"string","description":"必填，工作项类型, 枚举值必须通过list_workspace_work_item_types获取","properties":{}}},"required":["simple_name","work_item_type"]}

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
            toolset="meego",
            tool_name="mcp:meego_get_work_item_metadata",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
