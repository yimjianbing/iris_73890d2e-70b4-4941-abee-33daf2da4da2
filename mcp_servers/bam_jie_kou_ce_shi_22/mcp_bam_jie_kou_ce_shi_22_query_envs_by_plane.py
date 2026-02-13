"""
# `mcp:BAM 接口测试_22_query_envs_by_plane`

该工具用来查询psm对应部署的env环境

参数描述：
1. test_plane参数有两个取值，1代表线上控制面（如cn，i18n），2代表boe控制面（如cn boe，i18n boe），默认值取2，当用户输入指定需要获取线上(或者指定某个ppe env)数据时，此时值设置为1
2. psm填入用户输入的psm

返回值如果有返回多个env时，默认匹配用户指定的env，如果匹配不到则取 prod 这个env，如果还是没有则随机取第一个env

---

**Parameters Schema:**

{"type":"object","properties":{"psm":{"type":"string","properties":{},"format":""},"test_plane":{"type":"integer","properties":{},"format":""}}}

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
            tool_name="mcp:BAM 接口测试_22_query_envs_by_plane",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
