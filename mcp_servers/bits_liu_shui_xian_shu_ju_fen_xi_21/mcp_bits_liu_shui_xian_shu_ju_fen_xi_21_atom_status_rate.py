"""
# `mcp:Bits 流水线数据分析_21_atom_status_rate`

 该工具主要用于查询 Bits 原子(atom)一段时间内各状态数据占比情况。
通过提供start_time, end_time, atom_name, dimension,space_id,可以获取原子各状态的占比，返回的内容说明如下：
dimension: 维度信息
canceled_rate：取消率
failed_rate：失败率
rollbacked_rate：回滚率
skipped_rate：跳过率
successed_rate：成功率
job_status_change_to_canceled_times：取消次数
job_status_change_to_failed_times：失败次数
job_status_change_to_rollbacked_times：回滚次数
job_status_change_to_skipped_times：跳过次数
job_status_change_to_successed_times：成功次数
job_status_change_total：总次数

---

**Parameters Schema:**

{"type":"object","properties":{"atom_name":{"type":"string","description":"原子的名称","properties":{}},"dimension":{"type":"string","description":"聚合纬度,有month、weekly、day,分别代表按照月维度聚合、周纬度聚合、天纬度聚合","properties":{}},"end_time":{"type":"integer","description":"查询的结束时间，10位时间戳","properties":{}},"pipeline_scene_type":{"type":"array","description":"枚举值：有开发任务，发布单，流水线；也是筛选纬度之一，当选中多个的时候，表示或的逻辑","properties":{},"items":{"properties":{}}},"space_id":{"type":"integer","description":" 空间 id，也是筛选纬度之一","properties":{}},"start_time":{"type":"integer","description":"查询的开始时间，10位时间戳","properties":{}}},"required":["start_time","end_time","atom_name","dimension"]}

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
            tool_name="mcp:Bits 流水线数据分析_21_atom_status_rate",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
