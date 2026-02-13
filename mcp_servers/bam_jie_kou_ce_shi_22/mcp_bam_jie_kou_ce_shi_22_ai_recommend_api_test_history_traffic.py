"""
# `mcp:BAM 接口测试_22_ai_recommend_api_test_history_traffic`

该工具用来获取接口历史推荐流量
注意：当需要取获取接口的请求参数时，*必须*首先调用当前这个工具来进行获取，当工具的返回值为空或者data字段值为空时，需要再去调用 get_service_api_schema 这个工具去获取接口初始化参数

参数描述：
1. psm、http_method、http_path、protocol、function_name根据识别用户的输入进行自动填充

---

**Parameters Schema:**

{"type":"object","properties":{"function_name":{"type":"string","description":"方法名称","properties":{}},"http_method":{"type":"string","description":"当protocol=http时，GET/POST/DELETE/PUT/PATCH，全大写","properties":{}},"http_path":{"type":"string","description":"当protocol=http时，为URI路径","properties":{}},"protocol":{"type":"string","description":"协议类型,http/thrift","properties":{}},"psm":{"type":"string","description":"psm","properties":{}}},"required":["psm","protocol"]}

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
            toolset="BAM 接口测试_22",
            tool_name="mcp:BAM 接口测试_22_ai_recommend_api_test_history_traffic",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
