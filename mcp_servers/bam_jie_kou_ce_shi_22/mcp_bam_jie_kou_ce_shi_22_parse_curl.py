"""
# `mcp:BAM 接口测试_22_parse_curl`

该工具用来解析用户提供的curl脚本内容。
注意：
1. 【必须】需要先将用户提供的cURL 脚本内容（可能包含多行、注释和续行符）转换成一个单行的、合法的 cURL 命令字符串，并对字符串里的特殊字符进行转义处理符合json数据格式规范来构造出请求参数。
2. 如果识别到有多个cURL脚本内容，需要依次分别对每一个cURL脚本内容进行处理之后，来构造出最终的请求参数，字符串数组类型。
3. 工具返回的数据也是字符串数组类型，与传入的参数curl_list里的数组元素位置一一对应。
4. 如果返回的数据是空的，代表解析curl脚本内容异常。




---

**Parameters Schema:**

{"type":"object","properties":{"curl_list":{"type":"array","description":"根据用户提供的cURL脚本内容，在进行字符串内容转换/转义处理之后，符合json数据格式规范的cURL字符串内容列表","properties":{},"items":{"type":"string","description":"对每一个cURL脚本内容，进行字符串内容转换/转义处理之后，符合json数据格式规范的cURL字符串","properties":{},"format":""},"format":""}}}

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
            tool_name="mcp:BAM 接口测试_22_parse_curl",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
