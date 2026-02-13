"""
# `mcp:ByteFaaS_20_faas_get_service_by_psm`

输入 PSM 和 env_name，来查询对应 FaaS 服务的 meta 信息，包括 service_id，clusters 等等。可以通过这个 tool 来完成 PSM 到 service_id 的映射。

---

**Parameters Schema:**

{"type":"object","properties":{"env_name":{"type":"string","properties":{}},"psm":{"type":"string","properties":{}}},"required":["psm","env_name"]}

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
            tool_name="mcp:ByteFaaS_20_faas_get_service_by_psm",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
