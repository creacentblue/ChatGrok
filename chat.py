import os
import json
import requests
from typing import List, Dict

class GrokChat:
    def __init__(self):
        self.api_key = os.getenv('XAI_API_KEY')
        if not self.api_key:
            raise ValueError("Please set XAI_API_KEY environment variable")
        
        self.api_url = "https://api.x.ai/v1/chat/completions"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        self.conversation_history: List[Dict[str, str]] = [
            {
                "role": "system",
                "content": "You are a helpful AI assistant."
            }
        ]

    def chat(self, message: str) -> str:
        # Add user message to history
        self.conversation_history.append({
            "role": "user",
            "content": message
        })

        # Prepare the request
        payload = {
            "messages": self.conversation_history,
            "model": "grok-beta",
            "stream": False,
            "temperature": 0.7
        }

        # Make the API call
        try:
            response = requests.post(
                self.api_url,
                headers=self.headers,
                json=payload
            )
            response.raise_for_status()
            
            # Parse the response
            result = response.json()
            assistant_message = result['choices'][0]['message']['content']
            
            # Add assistant's response to history
            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_message
            })
            
            return assistant_message

        except requests.exceptions.RequestException as e:
            return f"Error: {str(e)}"

def main():
    chat = GrokChat()
    print("Grok Chat Interface (type 'quit' to exit)")
    print("-" * 50)

    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() in ['quit', 'exit']:
            break

        response = chat.chat(user_input)
        print("\nGrok:", response)

if __name__ == "__main__":
    main() 