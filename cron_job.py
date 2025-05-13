import os

CHAT_HISTORY_DIR = "Artifacts/chat_history"

if not os.path.exists(CHAT_HISTORY_DIR):
    print("Artifacts/chat_history does not exist. Skipping cleanup.")
else:
    for filename in os.listdir(CHAT_HISTORY_DIR):
        if filename.endswith(".json"):
            file_path = os.path.join(CHAT_HISTORY_DIR, filename)
            try:
                with open(file_path, 'w') as f:
                    f.write("")
            except Exception as e:
                print(f"Error clearing {file_path}: {e}")
