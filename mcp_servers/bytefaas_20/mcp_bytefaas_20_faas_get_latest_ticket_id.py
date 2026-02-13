"""
# `mcp:ByteFaaS_20_faas_get_latest_ticket_id`

这个是一个 FaaS 的 API，会根据给定的 FaaS 服务的 service_id, env 信息，来查询对应 FaaS 服务的最后的一次发布工单的 ID，ticket_id。通过 ticket_id 可以获取工单的信息。

---

**Parameters Schema:**

{"type":"object","properties":{"service_id":{"type":"string","properties":{}}},"required":["service_id"]}

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
            tool_name="mcp:ByteFaaS_20_faas_get_latest_ticket_id",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
