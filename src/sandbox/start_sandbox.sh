# 构建镜像
docker build -t noah-sandbox ./docker
# 启动容器（挂载本地data目录）
docker run -d --name noah-agent -v $(pwd)/data:/app/data noah-sandbox