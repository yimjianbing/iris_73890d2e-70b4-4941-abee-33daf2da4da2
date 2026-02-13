"""
# `mcp:lark_workspace_search_lark_meeting_doc`

搜索企业知识库中的会议纪要文档，包括文字记录、智能记录等，支持按项目、团队或个人维度检索指定时间段的会议纪要

---

**Parameters Schema:**

{"type":"object","properties":{"end_date":{"type":"string","description":"可选，查询结束日期，格式为YYYY-MM-DD","properties":{}},"project":{"type":"string","description":"可选，要查询的项目名称，比如：project123, 注意，并非所有工具都支持项目查询","properties":{}},"scope":{"type":"string","description":"可选，查询任务的覆盖面，可选值：personal/project，personal将会查询个人会议纪要，project将会查询项目相关的会议纪要","properties":{}},"start_date":{"type":"string","description":"可选，查询开始日期，格式为YYYY-MM-DD","properties":{}},"user_name":{"type":"string","description":"必填，要查询的用户名，强烈建议中英文混合已增强查询效果，比如：张三(zhangsan.001)","properties":{}}},"required":["project","user_name","start_date","end_date","scope"]}

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
            tool_name="mcp:lark_workspace_search_lark_meeting_doc",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
