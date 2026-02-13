"""
# `mcp:Bits 流水线数据分析_21_workflow_pipeline_run`

 该工具主要用于查询研发流程流水线运行情况。
通过提供workspace_id, process_workflow_id, template_id, node_id,process_from,start_time,end_time 可以获取研发流程流水线运行列表，返回的内容为列表，列表字段说明如下：
`build_time`: 一次运行的耗时，单位：s
`status`：构建状态，枚举值SUCCESS代表执行成功，CANCELLED代表执行失
`process_from`：项目类型，枚举值dev代表开发任务，rt代表发布单
`template_id`：模板id
`end_time`: 流水线运行结束时间，10位时间戳
`pipeline_waiting_duration`：流水线等待人工交互耗时，单位：s
`pipeline_failed_duration`：流水线等待重试操作耗时，单位：s

---

**Parameters Schema:**

{"type":"object","properties":{"end_time":{"type":"integer","description":"查询的结束时间,10位时间戳","properties":{}},"node_id":{"type":"integer","description":"节点ID","properties":{}},"process_from":{"type":"integer","description":"流程来源，1:发布单 10:开发任务","properties":{}},"process_workflow_id":{"type":"integer","description":"研发流程ID","properties":{}},"start_time":{"type":"integer","description":"查询的开始时间,10位时间戳","properties":{}},"template_id":{"type":"integer","description":"模版ID","properties":{}},"workspace_id":{"type":"integer","description":"空间ID","properties":{}}},"required":["start_time","end_time","workspace_id","process_workflow_id","template_id","node_id","process_from"]}

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
            toolset="Bits 流水线数据分析_21",
            tool_name="mcp:Bits 流水线数据分析_21_workflow_pipeline_run",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
