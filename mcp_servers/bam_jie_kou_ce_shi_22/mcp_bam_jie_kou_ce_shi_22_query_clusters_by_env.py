"""
# `mcp:BAM 接口测试_22_query_clusters_by_env`

这个工具用来根据env查询psm部署的cluster集群信息

参数描述：
1. test_plane参数有两个取值，1代表线上控制面（如cn，i18n），2代表boe控制面（如cn boe，
i18n boe），默认值取2，当用户输入指定需要获取线上数据时，此时值设置为1
2. psm获取用户输入的psm填充
3. env 通过获取 query_envs_by_plane 这个工具调用的返回值填充

返回值如果有多个，默认取值为cluster=default 的值（如果有），如果没有default，则随机取第一个值

---

**Parameters Schema:**

{"type":"object","properties":{"env":{"type":"string","properties":{},"format":""},"psm":{"type":"string","properties":{},"format":""},"test_plane":{"type":"integer","properties":{},"format":""}}}

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
            tool_name="mcp:BAM 接口测试_22_query_clusters_by_env",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
