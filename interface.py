import gradio as gr
from main import chat_with_ai
from voice import recognize_speech, text_to_speech

def voice_chat():
    """Handle voice input and output."""
    user_message = recognize_speech()
    ai_response = chat_with_ai(user_message, [])
    text_to_speech(ai_response)
    return ai_response

# Gradio Interface
with gr.Blocks() as demo:
    gr.Markdown("# Apna Chat - AI Chatbot")
    chat = gr.ChatInterface(chat_with_ai)
    voice_button = gr.Button("🎤 Speak").click(fn=voice_chat, outputs="text")
    demo.append(chat)
    demo.append(voice_button)

demo.launch()
