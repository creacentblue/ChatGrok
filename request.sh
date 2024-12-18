curl https://api.x.ai/v1/chat/completions -H "Content-Type: application/json" -H "Authorization: Bearer $XAI_API_KEY" -d '{
  "messages": [
    {
      "role": "system",
      "content": "You are a test assistant."
    },
    {
      "role": "user",
      "content": "Tell me something interesting."
    }
  ],
  "model": "grok-beta",
  "stream": false,
  "temperature": 0
}'