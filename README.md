# Local-Command-Line-Chatbot-using-Hugging-Face
Local Command-Line Chatbot using Hugging  Face It is a chatbot using Machine Learning Models to answer the questions
This is a **fully functional local chatbot** that runs in your terminal using a small Hugging Face text generation model. It maintains short-term memory to handle multi-turn conversations, and uses a sliding window to retain context.

> ✅ Runs locally  
> ✅ No GPU required  
> ✅ Based on `flan-t5-small`  
> ✅ Modular and easy to extend


#Project Structure
local-chatbot/
├── interface.py # CLI entry point
├── model_loader.py # Loads tokenizer and model
├── chat_memory.py # Maintains recent conversation context
└── README.md # Setup and usage guide

# OUTPUT EXAMPLE
Chatbot is ready! Type your message or /exit to quit.

User: What is the capital of France?
Bot: Paris
