import os
import sys
from pathlib import Path

MODEL_NAME = "gemini-2.0-flash"
SYSTEM_MESSAGE = "you're are a helpful assistant, summarize the given user message with respect to the chat history and explain the context of any specific words used, in as few lines as possible"

PATH_TO_CHAT_HISTORY = os.path.join("Artifacts", "chat_history")
PATH_TO_MODEL_SCHEMA = Path(os.path.join(os.getcwd(), "schemas", "response_schema.json"))