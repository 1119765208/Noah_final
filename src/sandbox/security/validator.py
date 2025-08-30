# 作用：在代码执行前拦截风险操作，符合 Manus “沙箱隔离危险命令” 的设计

import ast

def is_safe_code(code):
    # 禁止os.system、subprocess等危险函数调用
    forbidden_nodes = {
        ast.Call: [
            "os.system", "subprocess.run", "subprocess.Popen",
            "os.remove", "os.rmdir"  # 新增禁止文件删除操作
        ]
    }
    tree = ast.parse(code)
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            # 检查函数调用是否属于禁止列表
            func_name = ast.unparse(node.func)
            if func_name in forbidden_nodes[ast.Call]:
                return False, f"禁止调用危险函数：{func_name}"
    return True, "代码安全"