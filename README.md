# Notissue
Building a lightweight blog by the [issues] feature.

### Download

```sh
git clone git@github.com:importcjj/Notissue.git
```

### Build
```sh
cd notissue/
docker build -t jiaju.chen/blog:latest .
```

### Run
```sh
docker run -d -v /data/logs/notissue:/data/logs/notissue -p 0.0.0.0:7777:5000 --name blog jiaju.chen/blog
```
