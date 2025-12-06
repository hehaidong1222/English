#!/bin/bash

# 简单测试API是否正常工作
echo "Testing the TTS API..."

# 测试英语发音
curl -X POST http://localhost:8080/api/tts \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Hello world",
    "voice": "Cherry",
    "language_type": "English"
  }' --output /dev/null -w "HTTP Status: %{http_code}\n" -s

echo ""
echo "If you see HTTP Status: 200, the API is working correctly."