from src.agent.data_analyst.executor import run_task
from src.agent.model_api.base import ModelInterface


def main():
    api_key = input("请输入DeepSeek API密钥：")
    model = ModelInterface("deepseek", api_key)
    query = input("请输入数据分析需求（如“分析汽车MPG数据集的趋势”）：")
    result = run_task(query, model)
    print("执行结果：")
    if "error" in result:
        print(f"错误：{result['error']}")
    else:
        print(f"输出：{result['output']}")
        if "image" in result:
            print(f"图表已保存至：{result['image']}")

if __name__ == "__main__":
    main()