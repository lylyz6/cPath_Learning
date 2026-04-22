#!/bin/bash

# 1. 如果旧容器存在，先清理掉
docker rm -f cv_env

# 2. 启动新容器
docker run -itd \
  --name cv_env \
  --restart=always \
  --gpus all \
  --ipc=host \
  -p 8888:8888 \
  -v /mnt/i/CPath_Dataset:/workspace/data \
  -v /mnt/i/CPath_Code:/workspace/code \
  cpath_env:v2 \
  jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root --ServerApp.token='' --ServerApp.password=''