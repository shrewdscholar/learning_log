# 使用 Python 2.7 官方镜像
FROM python:2.7-slim

# 设置工作目录
WORKDIR /app

# 设置环境变量
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=learning_log.settings

# 安装系统依赖（如果需要）
RUN apt-get update && apt-get install -y \
    gcc \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# 先复制 requirements.txt 安装依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目所有文件
COPY . .

# 收集静态文件（如果 Django 有静态文件）
RUN python manage.py collectstatic --noinput || true

# 暴露端口
EXPOSE 8080

# 启动命令
CMD gunicorn learning_log.wsgi:application --bind 0.0.0.0:8080