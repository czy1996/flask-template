# flask-template
[![Build Status](http://101.132.32.187:8000/api/badges/czy1996/flask-template/status.svg)](http://101.132.32.187:8000/czy1996/flask-template)

flask 项目模板，使用docker compose

## Features

- docker-compose
- Drone CI

## Todo

- [x] 配置文件支持
- [x] 数据库及其配置文件
- [x] 部署流程编写/线上 compose 环境
- [x] logger 配置
- [ ] sample todo 
- [ ] json 数据验证, 错误自动返回 flask-marshmallow
- [ ] 分页逻辑
- [ ] 认证管理 flask-httpauth
- [ ] ~~响应钩子~~ 我也忘了这tm说的是啥


## 目的
本项目的目的是，以一个最小的实例，涵盖我不长的开发生涯中所遇到的问题，给出一个解决方案  
web 开发没有银弹，这份方案肯定不会适用于所有情况  

## 关于 Flask 全家桶
全家桶意思是，项目集成了很多第三方 Flask 扩展，来解决一些『套路性』的需求，如认证，ORM 等等。
之前受到别人的影响，是瞧不上 Flask 全家桶的，当然这么做确实有缺点。  

首先，大量使用扩展不适合初学者了解 web 开发的原理。其次，扩展的质量参差不齐。

经过了几个小项目的开发，我发现，尽管自己有能力在不使用扩展的情况下，手撸一份代码满足自己的需求，但实际上，代码会变得难以维护。  
这虽然是自己抽象能力不足的体现，但本质上，也是一种强行造轮子的行为。第三方扩展质量再怎么不稳定，恐怕也比我写得好，考虑的东西也比我多，遇到更高级的需求，扩展起来也更容易。  
但是，在开发的过程中，遇到没有想到过的问题，自己进行思考解决，也是一种锻炼的方式。

自己造轮子还是用别人的扩展，这两者如何权衡？本项目的目的，解决需求是第一位的，所以会尽量挑选好的扩展。  
对于『套路』性的需求，尽量探索成熟的解决方案。


## Notes

### 数据校验

我想实现的功能是，marshmallow 能够自动对 client 发过来的 json 进行校验，如果校验不通过，返回错误信息。
这样势必需要对每个请求定义一个合格的请求数据？~~因为从文档上来看，`schema.load`一定要所有的数据~~

marshmallow 主要用途是序列化和反序列化，是否真的需要这么重型的库？

再仔细分析一下，可能会遇到什么错误

- payload 一定是 JSON
- 字段缺失，对于每个 view，具体情况其实不一样。~~这只是意淫，其实想半天只有下面这种~~
不同的请求，需要对数据不一样，删除并不需要 content
显然只有 POST 才需要 load

```json
{
  "name": "fuck", // required,  
  "phone number": "shit", // required
  "address": , // optional
}
```

可选字段缺失不报错，必选字段缺失一定报错

## 说明

使用三套配置文件，根据 `APP_ENV` 环境变量进行切换

```shell
Development
Testing
Production
```

Pycharm 的运行可以添加环境变量，本地测试可以使用 virtualenv, 用的是开发数据库, 不加这个环境变量

```shell
(venv)$ pip install -r requirements.txt
(venv)$ pip install -e .

(venv)$ pytest
```

因为将整个包本地安装，所以导出安装包的时候应该这么做, 防止把 app 也写进去了

```shell
(venv)$ pip freeze --exclude-editable > requirements.txt
```

CI 测试在 .drone.yml 中配置了一个数据库

## 配置步骤

### 安装 Docker

### 安装 Drone



