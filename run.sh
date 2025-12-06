#!/bin/bash
# 启动英语单词学习网站

echo "正在启动英语单词学习网站..."
echo "请确保您已设置 DASHSCOPE_API_KEY 环境变量"

# 检查是否已设置API密钥
if [ -z "$DASHSCOPE_API_KEY" ]; then
    echo "警告: 未设置 DASHSCOPE_API_KEY 环境变量"
    echo "请先设置API密钥: export DASHSCOPE_API_KEY=your_actual_api_key"
fi

python app.py