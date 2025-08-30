# 基础镜像选择Python 3.12
FROM python:3.12-slim
# 安装常用数据科学库
RUN pip install pandas numpy matplotlib scikit-learn
# 创建工作目录，挂载外部卷（用于文件交互）
WORKDIR /app
VOLUME ["/app/data"]
# 限制网络访问（仅允许访问指定数据源，如HuggingFace Datasets）
RUN apt-get update && apt-get install -y iptables && \
    iptables -A OUTPUT -p tcp --dport 80 -j ACCEPT && \
    iptables -A OUTPUT -p tcp --dport 443 -j ACCEPT && \
    iptables -A OUTPUT -j DROP
# 启动命令（等待代码输入）
CMD ["bash"]