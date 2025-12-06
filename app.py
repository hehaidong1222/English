from flask import Flask, request, jsonify, send_file
from io import BytesIO
import os
import dashscope
import pyaudio
import base64
import numpy as np
from flask_cors import CORS
import tempfile
import wave

app = Flask(__name__)
CORS(app)  # 允许跨域请求

# 设置阿里云API基础URL
dashscope.base_http_api_url = 'https://dashscope.aliyuncs.com/api/v1'

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/api/tts', methods=['POST'])
def tts_api():
    try:
        data = request.json
        text = data.get('text', '')
        voice = data.get('voice', 'Cherry')
        language_type = data.get('language_type', 'English')
        
        # 使用阿里云Qwen3 TTS API
        api_key = os.getenv("DASHSCOPE_API_KEY")
        if not api_key:
            return jsonify({'error': 'DASHSCOPE_API_KEY not set'}), 400

        # 创建一个临时文件来保存音频数据
        import tempfile
        import wave
        
        # 使用流式API收集音频数据
        response = dashscope.MultiModalConversation.call(
            api_key=api_key,
            model="qwen3-tts-flash",
            text=text,
            voice=voice,
            language_type=language_type,
            stream=False  # 非流式响应以简化处理
        )

        if response and hasattr(response, 'output') and response.output and hasattr(response.output, 'audio') and response.output.audio and hasattr(response.output.audio, 'data') and response.output.audio.data:
            # 解码音频数据
            audio_data = base64.b64decode(response.output.audio.data)
            
            # 创建内存中的音频文件
            audio_buffer = BytesIO(audio_data)
            
            # 设置响应头为音频格式
            audio_buffer.seek(0)
            return send_file(
                audio_buffer,
                mimetype='audio/wav',
                as_attachment=False,
                download_name='pronunciation.wav'
            )
        else:
            return jsonify({'error': 'No audio data received from TTS API or invalid response structure'}), 500
            
    except Exception as e:
        print(f"Error in TTS API: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)