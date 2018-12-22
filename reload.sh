# 重新构建镜像, 只构建 pyweb, mongo 一般不去管
docker-compose -f docker-compose.yml build pyweb

# 这里还是根据官方文档的建议来吧
docker-compose up --no-deps -d web