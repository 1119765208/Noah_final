from src.sandbox.security.validator import is_safe_code


class CodeDebugger:
    def __init__(self, model_interface, max_retries=3):
        self.model_interface = model_interface
        self.max_retries = max_retries  # 最多重试3次（避免无限循环）

    def debug(self, original_code, error_msg, user_query):
        """基于错误信息修正代码"""
        for attempt in range(self.max_retries):
            # 构造调试Prompt（参考CodeAct图3的错误反馈模板）
            debug_prompt = f"""
            你之前生成的代码执行出错了！
            错误信息：{error_msg}
            原始需求：{user_query}
            原始代码：
            {original_code}
            请修正代码，确保：
            1. 解决上述错误；
            2. 代码可直接执行，无需人工修改；
            3. 仅返回修正后的代码，不添加解释。
            """
            # 调用模型生成修正代码
            fixed_code = self.model_interface.generate_code(debug_prompt)
            # 验证修正后的代码安全性
            is_safe, safe_msg = is_safe_code(fixed_code)
            if not is_safe:
                continue  # 不安全则重试
            # 返回修正后的代码
            return fixed_code
        # 超过最大重试次数，返回原始错误
        return None