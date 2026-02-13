"""
# `mcp:Bits 流水线数据分析_21_atom_error_detail`

该工具主要用于查询Bits 原子(atom)一段时间内运行失败列表数据。

通过提供start_time,end_time,atom_name,space_id,pipeline_scene_type 可以获取原子失败详情数据，包含atom_name,err_msg,error_msg_class_name,err_msg_label,fail_times,pipeline_url(失败的一例case)，下面是对返回字段说明：
* err_msg_class_name：错误类型，包含系统错误和业务错误 
  * 系统错误：不符合业务预期的报错，需要原子方去优化。 
  * 业务错误：符合业务预期的报错，需要使用方去优化。
* err_msg：报错信息，表示的是聚类后的错误信息。
* failed_times：报错次数，表示的是聚类后的错误信息，一共报错的次数。
* pipeline_url：一例失败的现场，是一个URL 链接, 表示聚类后的错误的一例现场，可用于给用户查看当时的现场情况。
* err_msg_label：错误分类标签，给这里错误定一个标签，方便归类。

---

**Parameters Schema:**

{"type":"object","properties":{"atom_name":{"type":"string","description":"原子名称","properties":{}},"end_time":{"type":"integer","description":"查询结束时间, 10位时间戳","properties":{}},"pipeline_scene_type":{"type":"array","description":"枚举值：有开发任务，发布单，流水线；也是筛选纬度之一，当选中多个的时候，表示或的逻辑","properties":{},"items":{"type":"string","properties":{}}},"space_id":{"type":"integer","description":"空间ID, 是筛选维度之一","properties":{}},"start_time":{"type":"integer","description":"查询开始时间, 10位时间戳","properties":{}}},"required":["start_time","end_time","atom_name"]}

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
            tool_name="mcp:Bits 流水线数据分析_21_atom_error_detail",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
