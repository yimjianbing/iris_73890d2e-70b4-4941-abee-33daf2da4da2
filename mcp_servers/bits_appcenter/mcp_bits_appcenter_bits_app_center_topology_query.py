"""
# `mcp:Bits-AppCenter_bits_app_center_topology_query`

查询服务调用链路

---

**Parameters Schema:**

{"type":"object","properties":{"knowledge_base_name":{"type":"string","description":"固定传Bits","properties":{}},"knowledge_graph_name":{"type":"string","description":"固定传resource_test","properties":{}},"query":{"type":"string","description":"可以提问调用链路相关的问题，用语言描述要获取的信息，包括服务和方法也可以模糊询问","properties":{}},"search_mode":{"type":"string","description":"固定传hybrid","properties":{}}},"required":["query","knowledge_base_name","knowledge_graph_name","search_mode"]}

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
            toolset="Bits-AppCenter",
            tool_name="mcp:Bits-AppCenter_bits_app_center_topology_query",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
