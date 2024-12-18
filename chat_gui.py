import os
import json
import requests
import tkinter as tk
from tkinter import ttk, scrolledtext
from typing import List, Dict
from chat import GrokChat

class GrokChatGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Grok Chat Interface")
        self.root.geometry("600x800")
        
        # Initialize the chat client
        self.chat_client = GrokChat()
        
        # Create main container
        self.main_container = ttk.Frame(root, padding="10")
        self.main_container.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        # Create chat display area
        self.chat_display = scrolledtext.ScrolledText(
            self.main_container,
            wrap=tk.WORD,
            width=60,
            height=30,
            font=("Arial", 10)
        )
        self.chat_display.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.chat_display.config(state=tk.DISABLED)
        
        # Create input field
        self.input_field = ttk.Entry(
            self.main_container,
            width=50,
            font=("Arial", 10)
        )
        self.input_field.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=10)
        self.input_field.bind("<Return>", self.send_message)
        
        # Create send button
        self.send_button = ttk.Button(
            self.main_container,
            text="Send",
            command=self.send_message
        )
        self.send_button.grid(row=1, column=1, sticky=(tk.E), padx=(10, 0), pady=10)
        
        # Configure grid weights
        self.main_container.columnconfigure(0, weight=1)
        self.main_container.rowconfigure(0, weight=1)
        
        # Welcome message
        self.append_to_chat("System: Welcome to Grok Chat! Type your message and press Enter or click Send.\n")

    def append_to_chat(self, message: str):
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, message + "\n")
        self.chat_display.see(tk.END)
        self.chat_display.config(state=tk.DISABLED)

    def send_message(self, event=None):
        message = self.input_field.get().strip()
        if not message:
            return
        
        # Clear input field
        self.input_field.delete(0, tk.END)
        
        # Display user message
        self.append_to_chat(f"You: {message}")
        
        # Get response from Grok
        try:
            response = self.chat_client.chat(message)
            self.append_to_chat(f"Grok: {response}")
        except Exception as e:
            self.append_to_chat(f"Error: {str(e)}")
        
        # Focus back on input field
        self.input_field.focus()

def main():
    root = tk.Tk()
    app = GrokChatGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main() 