"""
# `mcp:BAM 接口测试_22_check_code_coverage_span`

该工具用来检测对应psm、env下的代码覆盖率标签是否过期
注意：
调用这个工具前必须要先调用 query_clusters_by_env 这个工具来获取相关参数

参数描述：
1. env、online、psm、zone 参数填充依赖调用 query_clusters_by_env 这个工具来获取

---

**Parameters Schema:**

{"type":"object","properties":{"env":{"type":"string","description":"被测泳道，如ppe_test_plan","properties":{},"format":""},"ip_port":{"type":"string","description":"指定被测服务的ip port, 用于env缺失情况","properties":{},"format":""},"online":{"type":"boolean","description":"是否是线上测试场景","properties":{},"format":""},"psm":{"type":"string","properties":{},"format":""},"zone":{"type":"string","description":"区域","properties":{},"format":""}}}

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
            tool_name="mcp:BAM 接口测试_22_check_code_coverage_span",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
