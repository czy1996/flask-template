# flask-template
[![Build Status](http://101.132.32.187:8000/api/badges/czy1996/flask-template/status.svg)](http://101.132.32.187:8000/czy1996/flask-template)

flask 项目模板，使用docker compose

## Todo

- [x] 配置文件支持
- [x] 数据库及其配置文件
- [x] 部署流程编写/线上 compose 环境
- [x] logger 配置
- [ ] sample todo 
- [ ] json 数据验证, 错误自动返回
- [ ] 认证管理
- [ ] ~~响应钩子~~ 我也忘了这tm说的是啥 

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

Pycharm 的运行可以添加环境变量，本地测试可以使用 virtualenv, 用的是开发数据库

```shell
(venv)$ pip install -r requirements.txt
(venv)$ pip install -e .

(venv)$ pytest
```

因为将整个包本地安装，所以到处安装包的时候应该这么做

```shell
(venv)$ pip freeze --exclude-editable > requirements.txt
```

CI 测试在 .drone.yml 中配置了一个数据库

## 配置步骤

### 安装 Docker

### 安装 Drone



