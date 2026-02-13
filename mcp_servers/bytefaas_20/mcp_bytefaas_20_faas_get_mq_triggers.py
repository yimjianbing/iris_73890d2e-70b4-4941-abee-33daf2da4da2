"""
# `mcp:ByteFaaS_20_faas_get_mq_triggers`

输入 service_id, region, cluster, env 信息，来查询对应 faas 所有的 MQ Trigger 的 meta 信息。输出结果是1个 MQ Trigger 的 List，每个结果是1个 MQ Trigger 的 meta 信息。每个 MQ Trigger 包含的关键信息包括：options 里面的 topic 和 consumer_group 等。

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
            tool_name="mcp:ByteFaaS_20_faas_get_mq_triggers",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
