from model_loader import load_model
from chat_memory import ChatMemory

def run_chat():
    generator = load_model()
    memory = ChatMemory(window_size=3)
    print("Chatbot is ready! Type your message or /exit to quit.\n")

    while True:
        user_input = input("User: ").strip()
        if user_input.lower() == "/exit":
            print("Exiting chatbot. Goodbye!")
            break

        # Format using question-answer structure
        prompt = f"Question: {user_input}\nAnswer:"
        result = generator(prompt, max_new_tokens=100)[0]["generated_text"]

        print(f"Bot: {result.strip()}\n")
        memory.append(user_input, result.strip())

if __name__ == "__main__":
    run_chat()
