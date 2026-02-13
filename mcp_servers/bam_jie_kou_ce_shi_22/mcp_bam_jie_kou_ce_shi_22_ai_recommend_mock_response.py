"""
# `mcp:BAM 接口测试_22_ai_recommend_mock_response`

该工具用来获取接口历史响应数据
注意：如果需要获取一条线上真实测试流量的响应数据，历史流量响应数据，调用当前工具获取即可

参数描述：
1. mock_api，upstream_api这两个结构体都需要填充，结构题里面的psm、http_method、http_path、protocol、function_name根据识别用户的输入进行自动填充

---

**Parameters Schema:**

{"type":"object","properties":{"mock_api":{"type":"object","properties":{"function_name":{"type":"string","description":"方法名称","properties":{},"format":""},"http_method":{"type":"string","description":"当protocol=http时，GET/POST/DELETE/PUT/PATCH，全大写","properties":{},"format":""},"http_path":{"type":"string","description":"当protocol=http时，为URI路径","properties":{},"format":""},"idl_source":{"type":"integer","description":"idl来源","properties":{},"format":""},"idl_version":{"type":"string","description":"idl版本。IdlSource为Codebase时，为代码分支；IdlSource为Bam时，为Bam版本号","properties":{},"format":""},"protocol":{"type":"string","description":"协议类型,http/thrift","properties":{},"format":""},"psm":{"type":"string","description":"psm","properties":{},"format":""}},"required":["protocol","psm"],"format":""},"upstream_api":{"type":"object","properties":{"function_name":{"type":"string","description":"方法名称","properties":{},"format":""},"http_method":{"type":"string","description":"当protocol=http时，GET/POST/DELETE/PUT/PATCH，全大写","properties":{},"format":""},"http_path":{"type":"string","description":"当protocol=http时，为URI路径","properties":{},"format":""},"idl_source":{"type":"integer","description":"idl来源","properties":{},"format":""},"idl_version":{"type":"string","description":"idl版本。IdlSource为Codebase时，为代码分支；IdlSource为Bam时，为Bam版本号","properties":{},"format":""},"protocol":{"type":"string","description":"协议类型,http/thrift","properties":{},"format":""},"psm":{"type":"string","description":"psm","properties":{},"format":""}},"required":["psm","protocol"],"format":""}}}

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
            tool_name="mcp:BAM 接口测试_22_ai_recommend_mock_response",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
