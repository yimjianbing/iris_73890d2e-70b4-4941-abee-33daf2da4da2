"""
# `mcp:BAM 接口测试_22_rpc_request`

这个工具用来发起一次RPC接口请求测试
注意：
1. 【必须】如果用户直接指定了某个文件/或者指定了请求参数来触发一次测试，则直接调用这个工具发起一次RPC请求测试，否则*必须* 前置依赖调用  query_envs_by_plane、query_clusters_by_env、query_service_api_versions、check_code_coverage_span 、ai_recommend_api_test_history_traffic 这几个工具来获取相关参数。
2. 下面定义的参数都*必须*全部构造出来，才能调用 rpc_request 这个工具，在调用前需要对参数进行检查，如果缺少某些参数*必须*尝试再次调用相关工具获取。
3. 在填充参数时，请*务必*不要对参数进行额外转义，尤其是req_body，禁止对其进行额外的json字符串转义
4.【必须】当rpc_request工具正常执行返回数据后，*必须调用*analyze_api_test_result这个工具来进行测试结果分析，除非用户强制指定不需要进行结果分析。

参数描述：
1. psm、func_name依赖用户的输入值，识别psm及func_name
2. env 依赖调用 query_envs_by_plane 这个工具返回的结果
3. psm、idc、online、zone、cluster 依赖调用 query_clusters_by_env 这个工具返回的结果，5个参数都必须填充
4. idl_source、idl_version 依赖调用 query_service_api_versions 这个工具返回的结果，idl_source默认值取2
5. req_body 在进行工具调用时*必须*先调用 ai_recommend_api_test_history_traffic 这个工具来获取接口初始化参数，当返回值为空时，再调用当前 get_service_api_schema 这个工具来进行获取。*注意*：禁止对req_body参数进行额外json字符串转义，直接将参数进行填充


---

**Parameters Schema:**

{"type":"object","properties":{"address":{"type":"string","properties":{},"format":""},"bam_psm_cluster":{"type":"integer","description":"bam上的psm标签，即所属区域","properties":{},"format":""},"base":{"type":"object","description":"放一些请求基础信息","properties":{"inject_or_replace_jwt":{"type":"boolean","description":"注入或替换已有的jwt","properties":{},"format":""},"message_id_for_ai_request_example_code":{"type":"string","description":"假如使用了 Ai 生成 Request Example Code，则设置该字段为返回的 MessageId","properties":{},"format":""},"run_type":{"type":"integer","description":"测试请求执行模式","properties":{},"format":""},"tab_mock_key":{"type":"string","description":"当前测试页面Tab使用的mock分流key","properties":{},"format":""}},"format":""},"cluster":{"type":"string","properties":{},"format":""},"connect_timeout":{"type":"integer","properties":{},"format":""},"env":{"type":"string","properties":{},"format":""},"feature_id":{"type":"integer","properties":{},"format":""},"func_name":{"type":"string","properties":{},"format":""},"idc":{"type":"string","properties":{},"format":""},"idl_source":{"type":"integer","properties":{},"format":""},"idl_version":{"type":"string","properties":{},"format":""},"log_id":{"type":"string","properties":{},"format":""},"mock":{"type":"string","description":"是否为mock请求","properties":{},"format":""},"online":{"type":"boolean","properties":{},"format":""},"preset_env_id":{"type":"integer","properties":{},"format":""},"psm":{"type":"string","properties":{},"format":""},"req_body":{"type":"string","properties":{},"format":""},"request_id":{"type":"integer","properties":{},"format":""},"request_timeout":{"type":"integer","properties":{},"format":""},"rpc_context":{"type":"array","properties":{},"items":{"type":"object","properties":{"key":{"type":"string","properties":{},"format":""},"status":{"type":"integer","description":"是否启用","properties":{},"format":""},"type":{"type":"string","description":"透传类型","properties":{},"format":""},"value":{"type":"string","properties":{},"format":""}},"format":""},"format":""},"source":{"type":"integer","description":"发起请求的来源","properties":{},"format":""},"update_request":{"type":"boolean","description":"发送完是否更新当前集合中的当前请求","properties":{},"format":""},"zone":{"type":"string","properties":{},"format":""}}}

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
            tool_name="mcp:BAM 接口测试_22_rpc_request",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
