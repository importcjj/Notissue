# Notissue
Building a lightweight blog by the [issues] feature.

### Download

```sh
git clone git@github.com:importcjj/Notissue.git
```

### Build
```bash
cd notissue/
docker build -t jiaju.chen/blog:latest .
```

### Run
```sh
docker run -d -v /data/logs/notissue:/data/logs/notissue -p 0.0.0.0:7777:5000 --name blog jiaju.chen/blog
```

#### 我想要做的？
想法很简单，通过创建和编辑issue来触发webhooks，让github通知我的接口拉取指定repo的issue全量json数据，保存到sqlite中。把这些数据再做处理，做成博客。仔细想想之后，总是有种不三不四的感觉，比不上传统博客系统，如wordpree之流的大而全，也比不上静态博客框架的方便快捷。鸡肋鸡肋，食之无味！
