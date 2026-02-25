# 使用 Python 2.7 官方镜像
FROM python:2.7

# 设置工作目录
WORKDIR /app

# 设置环境变量
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=learning_log.settings

# 直接安装 Python 依赖（不安装系统包）
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目所有文件
COPY . .

# 暴露端口
EXPOSE 8080

# 启动命令
CMD gunicorn learning_log.wsgi:application --bind 0.0.0.0:8080