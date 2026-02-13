"""
# `mcp:BAM 接口测试_22_analyze_api_test_result`

该工具用来对一次测试请求结果进行结果分析
注意：
1. 【必须】这个工具的输出结果是sse流式格式，需要将 message_chunk 这个event类型的结果都拼在一起后再将分析结果进行包装统一输出，如果有代码相关内容请进行代码风格美化输出。
2. 【必须】当响应结果包含 "分析终止，请检查接口调试信息或者重新发起调试，再进行分析" 、"获取接口调试数据：失败"、"请重试" 之类的相关文案时，需要重新触发调用该工具。重试的时候修改api_test_ctrl_type的取值进行重试。*注意*：该工具最多只触发一次重试。
3. 【必须】当响应结果包含 "获取接口调试数据：成功"、"成功"之类的相关文案时，代表结果分析已经正常完成，不需要再重新触发执行了。

参数描述：
context_variables 是一个序列化后的json结构，json结构体定义如下：
{"api_test_history_id":480040783,"api_test_domain_type":"online","api_test_env_mod":"HTTP_Instance","api_test_ctrl_type":1}
api_test_history_id：取rpc_request或者http_request这两个工具的返回值里的 history_id 字段进行填充
api_test_ctrl_type：默认值取1，取rpc_request或者http_request这两个工具的返回值里的 online 字段进行判断，如果online字段的值为false时，该值设置为2
http_url_env_type：*必须*：当api_test_env_mod的值是HTTP_URL时，这个参数必须填。默认值取"online"，取rpc_request或者http_request这两个工具的返回值里的 online 字段进行判断，如果online字段的值为false时，该值设置为"offline"
api_test_domain_type：取默认值online
api_test_env_mod：根据用户的输入，如果触发的是RPC接口测试，则值为RPC，否则如果是Http接口测试，如果是指定了通过域名请求，则值为HTTP_URL，否则值为HTTP_Instance
请在一次接口测试执行结果完成后调用 analyze_api_test_result 这个工具，并填充参数来构造 context_variables

message_id、conversation_id：随机生成一个36位的UUID值进行参数填充。
input：默认填充 接口测试问题分析
intent：默认填充 测试结果分析

---

**Parameters Schema:**

{"type":"object","properties":{"context_variables":{"type":"string","properties":{}},"conversation_id":{"type":"string","properties":{}},"input":{"type":"string","properties":{}},"intent":{"type":"string","properties":{}},"message_id":{"type":"string","properties":{}}}}

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
            tool_name="mcp:BAM 接口测试_22_analyze_api_test_result",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
