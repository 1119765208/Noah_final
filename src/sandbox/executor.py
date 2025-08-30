import subprocess
import os
from datetime import datetime

class SandboxExecutor:
    def __init__(self, container_name="noah-sandbox"):
        self.container_name = container_name
        # 确保沙箱容器已启动（若未启动，自动启动）
        if not self._is_container_running():
            self._start_container()

    def _is_container_running(self):
        # 检查容器是否运行
        result = subprocess.run(
            ["docker", "ps", "--filter", f"name={self.container_name}", "--format", "{{.Names}}"],
            capture_output=True, text=True
        )
        return self.container_name in result.stdout

    def _start_container(self):
        # 启动Docker容器（基于Python 3.12镜像）
        subprocess.run([
            "docker", "run", "-d", "--name", self.container_name,
            "-v", f"{os.path.abspath('data')}:/app/data",  # 挂载本地data目录
            "noah-sandbox:latest"  # 镜像名需与Dockerfile构建结果一致
        ], check=True)

    def execute_code(self, code):
        """将代码注入沙箱执行，返回执行结果/错误"""
        # 生成唯一文件名（避免冲突）
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        code_filename = f"temp_code_{timestamp}.py"
        code_path = os.path.join("data", code_filename)

        # 写入代码到本地data目录（自动同步到沙箱）
        with open(code_path, "w") as f:
            f.write(code)

        # 在沙箱中执行代码
        result = subprocess.run(
            ["docker", "exec", self.container_name, "python", f"/app/data/{code_filename}"],
            capture_output=True, text=True
        )

        # 清理临时文件
        os.remove(code_path)

        # 返回执行结果（参考CodeAct对执行反馈的处理方式）
        return {
            "exit_code": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "success": result.returncode == 0
        }