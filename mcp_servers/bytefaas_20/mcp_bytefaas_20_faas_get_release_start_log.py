"""
# `mcp:ByteFaaS_20_faas_get_release_start_log`

这个是一个 FaaS 的 API，会根据给定的 FaaS 服务的 service_id, region, cluster, release_id 信息，来查询对应 FaaS 在对应的 release_id 的 release 的 pod 的启动日志, 其中 region 如果没有输入，那么就是 cn-north。pod 的 start_logs 字段包括的启动日志是排查 发布/启动 失败时的关键信息，一些失败的关键字：panic；error；exception；fail；

---

**Parameters Schema:**

{"type":"object","properties":{"cluster":{"type":"string","properties":{}},"region":{"type":"string","properties":{}},"release_id":{"type":"string","properties":{}},"service_id":{"type":"string","properties":{}}},"required":["service_id","region","cluster","release_id"]}

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
            toolset="ByteFaaS_20",
            tool_name="mcp:ByteFaaS_20_faas_get_release_start_log",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
