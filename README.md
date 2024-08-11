# NFL_IDNS_API 源代码库

## 关于本框架
- 重写消息收发模块,并修复了已知问题
- 全面推翻http协议,改用更安全的wss协议
- 基于websocket,响应更加迅速

## 工具准备
- Python 3.8.x(推荐)
- websocket-client
- 一双能动的手和一颗会思考的大脑 :thumbsup:  :thumbsup:  :thumbsup: 

## 安装
#### 通过git克隆
```
git clone https://gitee.com/nfl-tangh/nfl-idns-api.git
```

#### 通过pypi安装
```
pip install nfl_idns_api
```

## 代码示例
#### 导入模块
```python
from NFL_idns_api import NflIdnsLoader
```

#### 新建子类并重写父类函数
```python
class NflIdnsClient(NflIdnsLoader):
    def respondMsg(self, msg):
        if self.isinited:
            # 当有人发送 test 时回复 nflIdnsApi Program written by NFL_jiancx.
            if msg == "test": 
                self.sendText("nflIdnsApi Program written by NFL_jiancx.")
```

#### 创建刚刚定义的对象
```python
useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"
NFL_client = NflIdnsClient("NFL_Bot_test", "idns_cn", "CN", -1, useragent)
```

#### 最后别忘了启动主循环
```python
NFL_client.start()
```


## 开发人员
- NFL_jiancx
(别翻了,就这一位开发 :sweat_smile: )
