# 新增通义千问接口
class QwenAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"

    def generate_code(self, user_query):
        # 复用CodeAct的Prompt模板，确保不同模型生成代码格式一致
        prompt = f"""
        请生成能解决以下问题的Python代码（仅返回代码，无需解释）：
        {user_query}
        要求：
        1. 使用pandas处理数据，matplotlib可视化；
        2. 代码需保存结果到/app/data目录；
        3. 若需下载数据，直接使用URL读取（如pd.read_csv("https://...")）。
        """
        response = requests.post(
            self.url,
            headers={"Authorization": f"Bearer {self.api_key}"},
            json={
                "model": "qwen-max",
                "messages": [{"role": "user", "content": prompt}]
            }
        )
        return response.json()["choices"][0]["message"]["content"]


