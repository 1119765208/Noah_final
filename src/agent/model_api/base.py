# 统一接口
# 扩展ModelInterface支持多模型
# src/agent/model_api/base.py（补充）
from src.agent.model_api.deepseek import DeepSeekAPI
from src.agent.model_api.qwen import QwenAPI


class ModelInterface:
    def __init__(self, model_name, api_key):
        self.model_name = model_name
        if model_name == "deepseek":
            self.impl = DeepSeekAPI(api_key)
        elif model_name == "qwen":
            self.impl = QwenAPI(api_key)
        else:
            raise ValueError(f"不支持的模型：{model_name}")

    def switch_model(self, new_model_name, new_api_key):
        """动态切换模型（核心需求）"""
        self.__init__(new_model_name, new_api_key)