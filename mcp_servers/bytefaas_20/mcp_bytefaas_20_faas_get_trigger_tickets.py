"""
# `mcp:ByteFaaS_20_faas_get_trigger_tickets`

这个是一个 FaaS 的 API，会根据给定的 FaaS 服务的 service_id, region, cluster, env_name 信息，来查询对应 FaaS 服务的 MQ trigger 的发布记录。

---

**Parameters Schema:**

{"type":"object","properties":{"cluster":{"type":"string","properties":{}},"env_name":{"type":"string","properties":{}},"region":{"type":"string","properties":{}},"service_id":{"type":"string","properties":{}}},"required":["service_id","region","cluster","env_name"]}

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
            tool_name="mcp:ByteFaaS_20_faas_get_trigger_tickets",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
