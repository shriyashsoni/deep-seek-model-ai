# Apna Chat Bot

**Apna Chat Bot** is an AI-powered chatbot that uses DeepSeek/OpenAI models to generate intelligent responses. It supports multiple languages, including English, Hindi, and Punjabi. The bot can be deployed on Hugging Face, AWS, and integrated with WhatsApp and Telegram.

## Features
✅ AI Chat using DeepSeek/OpenAI models  
✅ Multilingual support (English, Hindi, Punjabi)  
✅ WhatsApp & Telegram bot integration  
✅ Cloud Deployment (Hugging Face & AWS)  
✅ Scalable & customizable AI responses  

---

## Installation & Setup

### **1. Clone the Repository**
```bash
git clone https://github.com/your-repo/apna-chat-bot.git
cd apna-chat-bot
```

### **2. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3. Set Up API Key**
- Open `model.py`
- Replace `your-api-key` with your DeepSeek/OpenAI API key

### **4. Run the Chatbot Locally**
```bash
python apna_chatbot.py
```

---

## Deployment Options

### **🌍 Deploy on Hugging Face**
1. Create an account on [Hugging Face](https://huggingface.co/)
2. Upload your `app.py` file
3. Deploy as a Gradio/Flask app

### **☁️ Deploy on AWS (EC2/Lambda)**
1. Launch an EC2 instance
2. Install dependencies using `pip install -r requirements.txt`
3. Run `gunicorn app:app --bind 0.0.0.0:5000`
4. Expose port 5000 for public access

---

## **📲 WhatsApp & Telegram Integration**

### **WhatsApp Bot Setup (Twilio API)**
1. Create a Twilio account
2. Get a Twilio WhatsApp sandbox number
3. Configure `whatsapp_bot.py` with Twilio credentials
4. Run the bot:  
   ```bash
   python whatsapp_bot.py
   ```

### **Telegram Bot Setup**
1. Create a bot using [BotFather](https://t.me/botfather)
2. Get the API token
3. Configure `telegram_bot.py` with the token
4. Run the bot:  
   ```bash
   python telegram_bot.py
   ```

---

## **Upcoming Features**
🔹 Voice chat support  
🔹 Database integration (Save chat history)  
🔹 Custom AI training (Fine-tune responses)  

---

## **🛠 Created By**
👤 **Shriyash Soni**  
📩 **Email:** [apnacounsellor@gmail.com](mailto:apnacounsellor@gmail.com)  
🌐 **Website:** [Apna Counsellor](https://www.apnacounsellor.com)  
