from collections import deque

class ChatMemory:
    def __init__(self, window_size=5):
        self.memory = deque(maxlen=window_size * 2)  # user + bot per turn

    def append(self, user_input, bot_response):
        self.memory.append(f"User: {user_input}")
        self.memory.append(f"Bot: {bot_response}")

    def get_context(self):
        return "\n".join(self.memory)
