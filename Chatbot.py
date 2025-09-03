import datetime
import random

jokes = [
    "😂 Why don’t scientists trust atoms? Because they make up everything!",
    "🤣 Why did the computer go to the doctor? Because it caught a virus!",
    "😅 Why don’t programmers like nature? It has too many bugs.",
    "🤭 Why did the math book look sad? Because it had too many problems."
]

quotes = [
    "💡 Believe you can and you're halfway there.",
    "🚀 The future depends on what you do today.",
    "🔥 Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "🌟 Push yourself, because no one else is going to do it for you."
]

def chatbot_response(user_input):
    user_input = user_input.lower()  

    if "hello" in user_input or "hi" in user_input:
        return "Hello! 👋 How can I help you today?"
    
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! Thanks for asking 😊"
    
    elif "weather" in user_input:
        return "I can't check live weather, but it's always sunny in my code world ☀️"
    
    elif "your name" in user_input:
        return "I'm HunarBot, your friendly internship chatbot 🤖"
    
    elif "date" in user_input:
        today = datetime.date.today()
        return f"Today's date is 📅 {today.strftime('%d %B %Y')}."
    
    elif "time" in user_input:
        now = datetime.datetime.now()
        return f"The current time is ⏰ {now.strftime('%I:%M %p')}."
    
    elif "day" in user_input:
        today = datetime.date.today()
        return f"Today is 🗓️ {today.strftime('%A')}."
    
    elif "joke" in user_input:
        return random.choice(jokes)
    
    elif "quote" in user_input or "motivation" in user_input:
        return random.choice(quotes)
    
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! 👋 Have a great day."
    
    else:
        return "Sorry, I don’t understand that yet. Please try asking something else."

print("🤖 HunarBot: Hello! Type 'bye' or 'exit' to end the chat.")

while True:
    user_query = input("You: ")
    response = chatbot_response(user_query)
    print("🤖 HunarBot:", response)
    
    if "bye" in user_query.lower() or "exit" in user_query.lower():
        break
