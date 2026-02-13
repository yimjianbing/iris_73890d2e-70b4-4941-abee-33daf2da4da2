"""
# `mcp:仓库说_23_get_rpcinfo`

获取向目标 psm 的目标 method 发起 RPC 调用的方式和相关信息。使用方式： 1. 将 psm 中的 . 替换为 _，下面的代码中使用 ${psm_} 代替。 2. 新增 import：code.byted.org/overpass/${psm_}/rpc/${psm_} 3. 发起调用代码为 resp, err := ${psm_}.RawCall.${method}(ctx, req)。如向 a.b.c 服务请求 Echo 方法的代码为： resp, err := a_b_c.RawCall.Echo(ctx, req) 新增的 import 为：import a_b_c "code.byted.org/overpass/a_b_c/rpc/a_b_c" 4. 结构体类型的定义为 ${package}:${type}，如果类型前有 *，则表示指针类型。基础类型如 bool、int32 等不会添加 package 前缀。 5. 枚举类型的定位为 ${package}:${type}=${value}，EnumValue 不为空则表示为 Enum 类型。 6. 我会将该方法的名称、Request、Response 结构体返回给你，以及结构体中的每个字段存放在 Fields 中，你可以按需使用。

---

**Parameters Schema:**

{"type":"object","properties":{"Method":{"type":"string","description":"方法名, 可选","properties":{},"format":""},"PSM":{"type":"string","description":"psm 名称","properties":{},"format":""}}}

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
            tool_name="mcp:仓库说_23_get_rpcinfo",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
