# 当 5070 Ti 到货并插好后，你只需要做两件事：
#在 Windows 装驱动，然后用一行带 --gpus all 的命令重起容器:
#在终端中运行:
# 1. 拆除目前的 CPU 版容器
docker rm -f cv_env

# 2. 启动 GPU 版容器（注意增加了 --gpus all 参数）
docker run -itd \
  --name cv_env \
  --restart=always \
  --gpus all \
  --ipc=host \
  -p 8888:8888 \
  -v /mnt/i/CPath_Dataset:/workspace/data \
  -v /mnt/i/CPath_Code:/workspace/code \
  cpath_env:v1 \
  jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root --ServerApp.token='' --ServerApp.password=''