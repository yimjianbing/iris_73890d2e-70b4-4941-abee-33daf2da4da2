"""
# `mcp:BAM 接口测试_22_http_request`

这个工具用来发起一次Http接口请求测试

注意：
1. 【必须】如果用户直接指定了某个文件/或者指定了请求参数来触发一次接口测试，则直接调用http_request这个工具发起一次Http请求测试，否则 *必须* 前置依赖调用  query_envs_by_plane、query_clusters_by_env、query_service_api_versions、check_code_coverage_span 、ai_recommend_api_test_history_traffic 这几个工具来获取相关参数。
2. 【必须】如果用户指定了请求参数来触发一次接口测试，并且请求参数里包含了*curl的脚本内容*，*必须* 需要先调用 parse_curl 这个工具来构造请求参数，然后直接调用http_request这个工具发起一次Http请求测试。如果parse_curl这个工具的data返回值里包含多个数据，那么需要分别对每一个数据直接调用http_request这个工具发起一次Http请求测试。如果parse_curl这个工具的data没有返回任何数据，则直接终止流程，不需要再调用其它任何工具。
3. 下面定义的参数都*必须*全部构造出来，才能调用 http_request 这个工具，在调用前需要对参数进行检查，如果缺少某些参数*必须*尝试再次调用相关工具获取。
4. 在填充参数时，请*务必*不要对参数进行额外转义，尤其是req_body，禁止对其进行额外的json字符串转义。
5. 【必须】当http_request工具正常执行返回数据后，*必须调用*analyze_api_test_result这个工具来进行测试结果分析，除非用户强制指定不需要进行结果分析。

参数描述：
1. env 依赖调用 query_envs_by_plane 这个工具返回的结果
2. 当识别到用户期望通过host域名方式来请求的时候，http_host 填充用户输入的域名，idc、online、zone、cluster 依赖调用query_clusters_by_env 这个工具返回的结果
3. idl_source、idl_version 依赖调用 query_service_api_versions 这个工具返回的结果，idl_source默认值取2
4. psm、func_name 依赖用户的输入值，识别psm及func_name
5. http_req_headers、http_cookies、http_query、http_path_params、form_req_body、req_body依赖调用 ai_recommend_api_test_history_traffic 这个工具来填充对应的参数。*注意*：禁止对req_body参数进行额外json字符串转义，直接将参数进行填充。http_req_headers、http_cookies、http_query、http_path_params、form_req_body 如果未获取到参数，默认值填[]
6. http_method、http_path 依赖用户的输入值，识别http_method及http_path


---

**Parameters Schema:**

{"type":"object","properties":{"address":{"type":"string","properties":{},"format":""},"bam_psm_cluster":{"type":"integer","description":"bam上的psm标签，即所属区域","properties":{},"format":""},"base":{"type":"object","description":"放一些请求基础信息","properties":{"inject_or_replace_jwt":{"type":"boolean","description":"注入或替换已有的jwt","properties":{},"format":""},"message_id_for_ai_request_example_code":{"type":"string","description":"假如使用了 Ai 生成 Request Example Code，则设置该字段为返回的 MessageId","properties":{},"format":""},"run_type":{"type":"integer","description":"测试请求执行模式","properties":{},"format":""},"tab_mock_key":{"type":"string","description":"当前测试页面Tab使用的mock分流key","properties":{},"format":""}},"format":""},"cluster":{"type":"string","properties":{},"format":""},"env":{"type":"string","properties":{},"format":""},"feature_id":{"type":"integer","description":"bam feature id","properties":{},"format":""},"form_req_body":{"type":"array","description":"form类型的请求体","properties":{},"items":{"type":"object","properties":{"desc":{"type":"string","properties":{},"format":""},"example":{"type":"string","properties":{},"format":""},"key":{"type":"string","properties":{},"format":""},"optional":{"type":"boolean","properties":{},"format":""},"status":{"type":"integer","description":"是否启用","properties":{},"format":""},"value":{"type":"string","properties":{},"format":""}},"format":""},"format":""},"func_name":{"type":"string","description":"idl方法名，序列化方法为protobuf时需要","properties":{},"format":""},"http_cookies":{"type":"array","properties":{},"items":{"type":"object","properties":{"desc":{"type":"string","properties":{},"format":""},"example":{"type":"string","properties":{},"format":""},"key":{"type":"string","properties":{},"format":""},"optional":{"type":"boolean","properties":{},"format":""},"status":{"type":"integer","description":"是否启用","properties":{},"format":""},"value":{"type":"string","properties":{},"format":""}},"format":""},"format":""},"http_host":{"type":"string","description":"http schema+host","properties":{},"format":""},"http_method":{"type":"string","description":"http方法","properties":{},"format":""},"http_path":{"type":"string","description":"http路径","properties":{},"format":""},"http_path_params":{"type":"array","properties":{},"items":{"type":"object","properties":{"desc":{"type":"string","properties":{},"format":""},"example":{"type":"string","properties":{},"format":""},"key":{"type":"string","properties":{},"format":""},"optional":{"type":"boolean","properties":{},"format":""},"status":{"type":"integer","description":"是否启用","properties":{},"format":""},"value":{"type":"string","properties":{},"format":""}},"format":""},"format":""},"http_query":{"type":"array","description":"query参数","properties":{},"items":{"type":"object","properties":{"desc":{"type":"string","properties":{},"format":""},"example":{"type":"string","properties":{},"format":""},"key":{"type":"string","properties":{},"format":""},"optional":{"type":"boolean","properties":{},"format":""},"status":{"type":"integer","description":"是否启用","properties":{},"format":""},"value":{"type":"string","properties":{},"format":""}},"format":""},"format":""},"http_req_headers":{"type":"array","description":"请求头","properties":{},"items":{"type":"object","properties":{"desc":{"type":"string","properties":{},"format":""},"example":{"type":"string","properties":{},"format":""},"key":{"type":"string","properties":{},"format":""},"optional":{"type":"boolean","properties":{},"format":""},"status":{"type":"integer","description":"是否启用","properties":{},"format":""},"value":{"type":"string","properties":{},"format":""}},"format":""},"format":""},"idc":{"type":"string","properties":{},"format":""},"idl_source":{"type":"integer","description":"idl来源","properties":{},"format":""},"idl_version":{"type":"string","description":"codebase分支或commitID或bam版本","properties":{},"format":""},"log_id":{"type":"string","description":"上游透传logid","properties":{},"format":""},"mock":{"type":"string","description":"是否为mock请求，True or False","properties":{},"format":""},"online":{"type":"boolean","properties":{},"format":""},"preset_env_id":{"type":"integer","properties":{},"format":""},"psm":{"type":"string","properties":{},"format":""},"req_body":{"type":"string","description":"请求体","properties":{},"format":""},"request_id":{"type":"integer","description":"请求ID","properties":{},"format":""},"request_timeout":{"type":"integer","description":"请求超时时间，http无法指定连接超时时间，需要申请工单","properties":{},"format":""},"serialization":{"type":"string","description":"序列化方法，json or protobuf or form","properties":{},"format":""},"source":{"type":"integer","description":"发起请求的来源","properties":{},"format":""},"update_request":{"type":"boolean","description":"发送完是否更新当前集合中的当前请求","properties":{},"format":""},"zone":{"type":"string","description":"地区","properties":{},"format":""}}}

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
            tool_name="mcp:BAM 接口测试_22_http_request",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
