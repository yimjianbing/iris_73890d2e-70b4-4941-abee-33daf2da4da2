"""
# `mcp:Bits 流水线数据分析_21_client_mr_count`

该工具主要用户查询Bits客户端MR(merge request)一段时间内的数量，通过提供app_id,start_time,end_time,dimension,mr_state来获取创建的MR数量，返回内容说明如下：
dimension: 维度信息
mr_total:mr数量

---

**Parameters Schema:**

{"type":"object","properties":{"app_id":{"type":"number","description":"Bits空间对应的app_id","properties":{}},"dimension":{"type":"string","description":"聚合纬度,有month, weekly 和 day,分别代表按照月维度聚合，周纬度聚合和天纬度聚合","properties":{}},"end_time":{"type":"number","description":"查询的结束时间，10位时间戳","properties":{}},"mr_state":{"type":"array","description":"mr状态,包含三个状态: opened,closed,merged","properties":{},"items":{"type":"string","properties":{}}},"start_time":{"type":"number","description":"查询的开始时间，10位时间戳","properties":{}}},"required":["app_id","start_time","end_time","dimension"]}

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
            tool_name="mcp:Bits 流水线数据分析_21_client_mr_count",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
