from src.sandbox.security.validator import is_safe_code

# 测试用例1：包含危险函数os.system
unsafe_code = """
import os
os.system("rm -rf /")
"""
safe, msg = is_safe_code(unsafe_code)
print(f"测试1（危险代码）：{msg}")  # 预期输出：禁止调用危险函数：os.system

# 测试用例2：安全的数据分析代码
safe_code = """
import pandas as pd
df = pd.read_csv("data/iris.csv")
print(df.mean())
"""
safe, msg = is_safe_code(safe_code)
print(f"测试2（安全代码）：{msg}")  # 预期输出：代码安全