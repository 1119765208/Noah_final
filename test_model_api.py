from src.agent.model_api.base import ModelInterface

# 初始化DeepSeek模型（替换为你的API密钥）
model = ModelInterface("deepseek", api_key="你的DeepSeek密钥")
# 测试需求（参考CodeAct的Tabular Reasoning任务）
query = "分析https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv数据集，计算不同性别顾客的平均消费额，并绘制柱状图保存到/app/data/tips_plot.png"
code = model.generate_code(query)
print("生成的代码：")
print(code)