from src.sandbox.executor import SandboxExecutor

executor = SandboxExecutor()
# 执行简单代码（生成测试文件）
test_code = """
with open("/app/data/test_output.txt", "w") as f:
    f.write("沙箱执行测试成功")
"""
result = executor.execute_code(test_code)
print(f"执行结果：{result['stdout']}")  # 预期无错误输出
# 检查宿主机data目录是否生成文件
import os
assert os.path.exists("data/test_output.txt"), "沙箱文件未同步到本地"