"""
# `mcp:ByteFaaS_20_faas_get_cluster`

这个是一个 FaaS 的 API，会根据给定的 FaaS 服务的 service_id, region, cluster, env信息，来查询对应 FaaS 服务的很多配置信息。region 如果没有输入，那么就是 cn-north。

---

**Parameters Schema:**

{"type":"object","properties":{"cluster":{"type":"string","properties":{}},"region":{"type":"string","properties":{}},"service_id":{"type":"string","properties":{}}},"required":["service_id","region","cluster"]}

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
            tool_name="mcp:ByteFaaS_20_faas_get_cluster",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
