def parse_query(query):
    # 示例：从用户输入中提取URL和任务类型
    if "分析" in query and "数据集" in query:
        return {
            "data_url": extract_url(query),  # 从query中提取数据源URL
            "task_type": "trend_analysis"  # 分析类型（趋势/分布等）
        }