"""
# `mcp:ByteFaaS_20_faas_get_latest_release`

这个是一个 FaaS 的 API，会根据给定的 FaaS 服务的 service_id, region, cluster, env信息，来查询对应 FaaS 服务的最后的一次发布记录,其中 region 如果没有输入，那么就是 cn-north。正常情况下，用户反馈发布失败，如果没有指定特定的工单 ticket_id, 指的是最后一次发布。返回的发布记录包含了发布的信息，本次发布的 release_id（对应的 key 是 release_id), 发布状态，失败原因，对应的发布工单的 ticket_id。

---

**Parameters Schema:**

{"type":"object","properties":{"cluster":{"type":"string","properties":{}},"region":{"type":"string","properties":{}},"service_id":{"type":"string","properties":{}}},"required":["service_id","region"]}

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
            tool_name="mcp:ByteFaaS_20_faas_get_latest_release",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
