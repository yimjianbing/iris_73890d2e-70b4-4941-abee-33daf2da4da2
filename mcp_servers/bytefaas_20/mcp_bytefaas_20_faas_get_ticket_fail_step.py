"""
# `mcp:ByteFaaS_20_faas_get_ticket_fail_step`

这个是一个 FaaS 的 API，会根据给定的 FaaS 服务的 service_id, ticket_id, env 信息，来查询对应 FaaS 服务的发布工单的失败的 step。1 个 release 发布属于 1 个 ticket 工单。其中 step 的 step_progress 包含 step 失败的关键信息和可能的原因。

---

**Parameters Schema:**

{"type":"object","properties":{"service_id":{"type":"string","properties":{}},"ticket_id":{"type":"string","properties":{}}},"required":["service_id","ticket_id"]}

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
            tool_name="mcp:ByteFaaS_20_faas_get_ticket_fail_step",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
