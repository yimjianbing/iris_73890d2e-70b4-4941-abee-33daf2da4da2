"""
# `mcp:BAM 接口测试_22_query_service_api_versions`

该工具用来查询psm对应idl api版本信息

参数描述
1. psm获取用户填入的psm值
2. bam_psm_cluster 取默认值 0
3. idl_repo_branch 取默认值 master

返回结果如果有多个，默认取数组里idl_branch=master最前的一个version值

---

**Parameters Schema:**

{"type":"object","properties":{"bam_psm_cluster":{"type":"integer","description":"bam上的psm标签，即所属区域","properties":{},"format":""},"idl_repo_branch":{"type":"string","description":"idl分支，填了则返回该psm在这个分支下的api版本，否则返回该psm的所有api版本","properties":{},"format":""},"psm":{"type":"string","properties":{},"format":""}}}

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
            tool_name="mcp:BAM 接口测试_22_query_service_api_versions",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
