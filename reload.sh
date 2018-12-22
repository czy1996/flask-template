# 重新构建镜像, 只构建 pyweb, mongo 一般不去管
docker-compose -f docker-compose.yml build pyweb

# 只关闭 pyweb
docker-compose stop pyweb

# 启动
# 其实我觉得这里 mongo 也重启了，但数据应该不会丢，down 会丢失数据
# restart always 怎么办
docker-compose up -d