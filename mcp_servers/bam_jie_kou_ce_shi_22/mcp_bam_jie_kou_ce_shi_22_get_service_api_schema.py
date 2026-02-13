"""
# `mcp:BAM 接口测试_22_get_service_api_schema`

该工具用来获取psm对应接口初始化参数
注意：在调用当前get_service_api_schema这个工具时，*必须* 首先去调用ai_recommend_api_test_history_traffic这个工具去获取接口初始化推荐参数，只有当ai_recommend_api_test_history_traffic这个工具获取不到值或者为空时，再调用get_service_api_schema这个工具来获取

参数描述：
1. psm、http_method、http_path、func_name根据识别用户的输入进行自动填充
2. idl_source、idl_version 依赖调用query_service_api_versions这个工具进行获取，idl_source默认值取2
3. test_plane参数有两个取值，1代表线上控制面（如cn，i18n），2代表boe控制面（如cn boe，i18n boe），默认值取2，当用户输入指定需要获取线上数据时，此时值设置为1
4. source默认值取1
5. bam_psm_cluster默认值取1
6. reset默认值取0
7. serialization取默认值json

---

**Parameters Schema:**

{"type":"object","properties":{"bam_psm_cluster":{"type":"integer","description":"bam上的psm标签，即所属区域","properties":{},"format":""},"func_name":{"type":"string","description":"如果是rpc接口，则需要传func_name","properties":{},"format":""},"http_method":{"type":"string","description":"如果是http接口，则需要传path和method","properties":{},"format":""},"http_path":{"type":"string","description":"如果是http接口，则需要传path和method","properties":{},"format":""},"idl_source":{"type":"integer","properties":{},"format":""},"idl_version":{"type":"string","properties":{},"format":""},"method":{"type":"string","description":"废弃","properties":{},"format":""},"path":{"type":"string","description":"废弃","properties":{},"format":""},"psm":{"type":"string","properties":{},"format":""},"reset":{"type":"integer","description":"测试参数重置为空\ndefulat 0","properties":{},"format":""},"serialization":{"type":"string","description":"HTTP序列化方式 json or protobuf or form, 仅form会特殊处理","properties":{},"format":""}}}

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
            tool_name="mcp:BAM 接口测试_22_get_service_api_schema",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
