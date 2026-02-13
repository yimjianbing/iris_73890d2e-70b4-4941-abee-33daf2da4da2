"""
# `mcp:lark_workspace_search_lark_doc`

按时间范围检索飞书文档，返回指定时间段内的文档列表供进一步筛选。支持按项目、团队或个人维度查询。注意：不要使用此工具检索会议纪要，会议纪要请使用 search_lark_meeting_doc 工具

---

**Parameters Schema:**

{"type":"object","properties":{"context_task":{"type":"string","description":"optional, 任务描述，简要描述任务内容，工具会在搜索的同时分析文档和变更记录与这个任务描述的相关性，并返回和任务的相关性说明，没有字数和语法限制","properties":{}},"end_date":{"type":"string","description":"必填，查询结束日期，格式为YYYY-MM-DD","properties":{}},"project":{"type":"string","description":"当scope为project时必填，要查询的项目名称，比如：project123","properties":{}},"scope":{"type":"string","description":"必填，查询文档的范围，可选值：personal（个人文档）/project（项目文档）","properties":{}},"start_date":{"type":"string","description":"必填，查询开始日期，格式为YYYY-MM-DD","properties":{}},"user_name":{"type":"string","description":"当scope为personal时必填，要查询的用户名，必须是ID，可以搜索非当前用户的文档，严禁其他格式或者中英文混搭，正确例子：zhangsan.001","properties":{}}},"required":["scope","user_name","project","start_date","end_date"]}

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
            tool_name="mcp:lark_workspace_search_lark_doc",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
