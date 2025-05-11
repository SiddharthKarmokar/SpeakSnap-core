import os
import json
from typing import List

def save_chat_history(path: str, chat_history: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True) 
    with open(path, 'w', encoding='utf-8') as f:
        json.dump({"chat_history": chat_history}, f, indent=2)

def load_chat_history(path: str) -> dict:
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)
