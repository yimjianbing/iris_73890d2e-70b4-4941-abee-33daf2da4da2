"""
# `mcp:lark_workspace_list_lark_task`

List all tasks assigned to a specific user in Lark.

---

**Parameters Schema:**

{"type":"object","properties":{"end_date":{"type":"string","description":"可选，查询结束日期，格式为YYYY-MM-DD","properties":{}},"project":{"type":"string","description":"可选，要查询的项目名称，比如：project123, 注意，并非所有工具都支持项目查询","properties":{}},"scope":{"type":"string","description":"可选，查询任务的覆盖面，可选值：personal/team，personal将会查询个人任务，team将会从用户任务列表查询关联清单，并查询清单中所有人的任务列表","properties":{}},"start_date":{"type":"string","description":"可选，查询开始日期，格式为YYYY-MM-DD","properties":{}},"user_email":{"type":"string","description":"必填，要查询的用户邮箱账号，比如：user@example.com","properties":{}}},"required":["project","user_email","start_date","end_date","scope"]}

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
            toolset="lark_workspace",
            tool_name="mcp:lark_workspace_list_lark_task",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
