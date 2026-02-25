#!/bin/sh

echo "========================================="
echo "🚀 启动脚本开始执行..."
echo "========================================="

echo "当前时间: $(date)"
echo "DATABASE_URL: $DATABASE_URL"

echo "🔄 正在执行数据库迁移..."
python manage.py migrate --noinput

# 检查是否有 data.json 文件
if [ -f data.json ]; then
    echo "📄 找到 data.json, 正在导入数据..."
    python manage.py loaddata data.json
    if [ $? -eq 0 ]; then
        echo "✅ 数据导入成功！"
    else
        echo "❌ 数据导入失败！"
    fi
else
    echo "⚠️ 没有找到 data.json, 跳过数据导入"
fi

echo "🚀 正在启动 Gunicorn..."
exec gunicorn learning_log.wsgi:application --bind 0.0.0.0:8080