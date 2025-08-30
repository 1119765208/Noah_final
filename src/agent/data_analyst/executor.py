from src.agent.data_analyst.debugger import CodeDebugger


def run_task(query, model_interface, sandbox_executor):
    # 1. 解析需求→2. 生成代码→3. 安全验证（省略）
    # 4. 执行代码
    execution_result = sandbox_executor.execute_code(code)
    if not execution_result["success"]:
        # 初始化调试器
        debugger = CodeDebugger(model_interface)
        # 尝试修正代码
        fixed_code = debugger.debug(
            original_code=code,
            error_msg=execution_result["stderr"],
            user_query=query
        )
        if fixed_code:
            # 执行修正后的代码
            return sandbox_executor.execute_code(fixed_code)
        else:
            return {"error": f"超过最大重试次数：{execution_result['stderr']}"}
    return execution_result