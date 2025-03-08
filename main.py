from model import generate_response

HISTORY_FILE = "history.txt"

def save_chat_history(user_message, ai_response):
    """Save chat history to a file."""
    with open(HISTORY_FILE, "a") as file:
        file.write(f"User: {user_message}\nAI: {ai_response}\n\n")

def chat_with_ai(message, history):
    """Generate AI response and store chat history."""
    history_text = "\n".join([f"User: {h[0]}\nAI: {h[1]}" for h in history])
    prompt = f"{history_text}\nUser: {message}\nAI:"
    response = generate_response(prompt)
    save_chat_history(message, response)
    return response
