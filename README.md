# flask-template
[![Build Status](http://101.132.32.187:8000/api/badges/czy1996/flask-template/status.svg)](http://101.132.32.187:8000/czy1996/flask-template)

flask 项目模板，使用docker compose

## Todo

- [x] 配置文件支持
- [x] 数据库及其配置文件
- [ ] 部署流程编写/线上 compose 环境

## Features

- docker-compose
- Drone CI

## 说明

使用三套配置文件，根据 `APP_ENV` 环境变量进行切换

```shell
Development
Testing
Production
```

Pycharm 的运行可以添加环境变量，本地测试可以使用 virtualenv

```shell
$ pip install -r requirements.txt
$ pip install -e .

$ pytest
```

CI 测试在 .drone.yml 中配置了一个数据库

## 配置步骤

### 安装 Docker

### 安装 Drone



