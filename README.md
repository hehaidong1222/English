# 英语单词学习网站

这是一个使用阿里云Qwen3 TTS API的英语单词学习网站，具有自动发音功能。

## 功能特性

- 单词卡片显示（英语单词、音标、中文翻译）
- 自动播放英语和中文发音
- 上一个/下一个单词导航
- 手动播放按钮
- 使用阿里云Qwen3高质量语音合成

## 环境要求

- Python 3.7+
- 阿里云DashScope API密钥

## 安装步骤

1. 安装依赖包：
   ```bash
   pip install -r requirements.txt
   ```

2. 设置API密钥环境变量：
   ```bash
   export DASHSCOPE_API_KEY=your_actual_api_key
   ```

3. 运行应用：
   ```bash
   ./run.sh
   ```
   
   或者直接运行：
   ```bash
   python app.py
   ```

## 访问网站

应用启动后，访问 http://localhost:8080 即可使用网站。

## 项目结构

- `app.py` - Flask后端服务
- `index.html` - 前端界面
- `requirements.txt` - 依赖包列表
- `run.sh` - 启动脚本

## API说明

后端提供TTS（文本转语音）API接口：
- 端点：`/api/tts`
- 方法：POST
- 参数：text, voice, language_type

## 注意事项

- 确保网络连接正常，以便访问阿里云API
- API密钥请妥善保管，不要泄露
- 首次访问可能需要稍长加载时间