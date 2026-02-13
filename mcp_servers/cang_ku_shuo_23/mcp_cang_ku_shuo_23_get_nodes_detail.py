"""
# `mcp:仓库说_23_get_nodes_detail`

精确获取指定 函数（FUNC）、类型（TYPE）、变量（VAR） 的详细信息，包括代码、类型、文件位置以及和其它节点的关系如：依赖（Dependencies)、引用（References)、实现（Implements) 等。
nodes_id 拼接方式为: ${go_module_name}?${package_name}#{name}。
go_module_name 是 go mod 中的名称，通常情况下和 reponame 相同；
package_name 是包名称；
name：对于变量、类型、函数，name 就是名称；对于结构体方法，name 为${结构体名称}.${方法名}。
当你缺少上述信息时，你可以通过 get_repos_detail -> get_packages_detail -> get_nodes_detail 的方式获取 nodes 信息。

---

**Parameters Schema:**

{"type":"object","properties":{"need_related_codes":{"type":"boolean","description":"indicate whether return the codes of related nodes","properties":{}},"node_ids":{"type":"array","description":"the node ids","properties":{},"items":{"type":"string","description":"the identity of node, in format of [ModPath]?\u003cPkgPath\u003e#\u003cSymName\u003e'. (NOTICE: PkgPath must be full package path)","properties":{}}},"repo_name":{"type":"string","description":"the repository name","properties":{}}},"required":["repo_name","node_ids","need_related_codes"]}

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
            toolset="仓库说_23",
            tool_name="mcp:仓库说_23_get_nodes_detail",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
