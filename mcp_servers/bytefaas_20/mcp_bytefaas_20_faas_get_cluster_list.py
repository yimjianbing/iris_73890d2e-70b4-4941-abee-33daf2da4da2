"""
# `mcp:ByteFaaS_20_faas_get_cluster_list`

输入 service_id, region, env 信息，来查询对应 FaaS 服务所有的 cluster。

---

**Parameters Schema:**

{"type":"object","properties":{"region":{"type":"string","properties":{}},"service_id":{"type":"string","properties":{}}},"required":["service_id","region"]}

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
            tool_name="mcp:ByteFaaS_20_faas_get_cluster_list",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
