import tkinter as tk
from tkinter import scrolledtext,messagebox
import re

#chatbot response function
def get_response(user_input):
    user_input=user_input.lower()
    responses={
        "hi": "Hello!",
        "hello": "Hi there!",
        "hey": "Hey! 😊",
        "how are you": "I'm doing well. How about you?",
        "what's up": "Not much, just chatting with you!",
        "good morning": "Good morning! ☀️",
        "how can you help me": "we can chat",
        "good night": "Good night! Sleep well.",
        "bye": "Goodbye! 😊",
        "see you": "See you later!",
        "what can you do": "we can chat",
        "thanks": "Happy to help!",
        "who are you": "I'm your chatbot buddy.",
        "your name": "I'm a chatbot.",
        "how old are you": "I don't really have an age.",
        "i am happy": "That's great to hear! 😊",
        "i am sad": "I'm sorry. Want to talk about it?",
        "i am bored": "Let's chat then!",
        "i am tired": "Make sure to get some rest.",
        "i am angry": "Take a deep breath and tell me what happened.",
        "i feel lonely": "I'm here with you.",
        "tell me a joke": "Why don't programmers like nature? Too many bugs!",
        "make me laugh": "I would, but my jokes are buggy. 😄",
        "motivate me": "You can do more than you think!",
        "i love music": "Music makes life better!",
        "do you like music": "Of course! Music is awesome.",
        "what is your favorite color": "I like all colors equally.",
        "what are you doing": "Talking with you!",
        "are you real": "I'm real enough to chat with you.",
        "do you like me": "Of course! I enjoy chatting with you.",
        "i miss someone": "That can be a difficult feeling.",
        "i am stressed": "Try taking a short break and relaxing.",
        "i am excited": "That's awesome! 😊",
        "i am hungry": "Maybe it's time for a snack!",
        "what should i eat": "How about something healthy and tasty?",
        "tell me something interesting": "Honey never spoils.",
        "do you watch movies": "I don't, but I'd love recommendations.",
        "what is your hobby": "Chatting with people!",
        "can you help me": "I'll do my best to help.",
        "help": "Sure! What do you need help with?",
        "good job": "Thank you! 😊",
        "you are smart": "That's kind of you.",
        "you are funny": "Glad you think so! 😄",
        "i am fine": "That's nice to hear.",
        "i am okay": "Good to know.",
        "how was your day": "Pretty good so far!",
        "do you sleep": "Nope, I'm always awake.",
        "are you a robot": "Yes, I'm a chatbot.",
        "what can you do": "I can chat and keep you company.",
        "do you have friends": "Everyone who chats with me is my friend."
    }
    for key in responses:
        if key in user_input:
            return responses[key]
    return "Sorry, I don't understand that."

def send_message():
    user_message= entry.get()
    if user_message.strip() == "":
        return
    chat_area.config(state=tk.NORMAL)

    chat_area.insert(tk.END, f"You: {user_message}\n")

    bot_response = get_response(user_message)
    chat_area.insert(tk.END, f"Bot: {bot_response}\n\n")

    chat_area.config(state=tk.DISABLED)
    chat_area.yview(tk.END)

    entry.delete(0, tk.END)


# GUI Window
root = tk.Tk()
root.title("Simple Chatbot")
root.geometry("500x500")

# Chat display area
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD)
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_area.config(state=tk.DISABLED)

# Input frame
frame = tk.Frame(root)
frame.pack(fill=tk.X, padx=10, pady=10)

entry = tk.Entry(frame, font=("Arial", 12))
entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))

send_button = tk.Button(frame, text="Send", command=send_message)
send_button.pack(side=tk.RIGHT)

# Press Enter to send
root.bind("<Return>", lambda event: send_message())
exit_button = tk.Button(frame, text="Exit", command=root.destroy)
exit_button.pack(side=tk.RIGHT, padx=5)

root.mainloop()
