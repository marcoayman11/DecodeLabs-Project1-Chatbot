
import random
from datetime import datetime

# =========================
# Chatbot Responses
# =========================

greetings = ["Hello!", "Hi there!", "Hey!"]
how_are_you_responses = [
    "I'm doing great!",
    "Everything is running smoothly!",
    "I'm fine, thanks for asking!"
]

unknown_responses = [
    "I don't understand that.",
    "Can you say that differently?",
    "Interesting... tell me more."
]

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "I told my computer I needed a break, and it said 'No problem — I'll freeze.'",
    "Python is my favorite snake."
]

# =========================
# Chatbot Function
# =========================

def chatbot_response(user_input):

    user_input = user_input.lower().strip()
    user_name = ""

    # Greetings
    if user_input in ["hi", "hello", "hey"]:
        return random.choice(greetings)

    # Asking bot name
    elif "your name" in user_input:
        return "My name is SmartBot."
    
    
    elif "my name is" in user_input:
       user_name = user_input.replace("my name is", "").strip()
       return f"Nice to meet you, {user_name}"

    # Asking how are you
    elif "how are you" in user_input:
        return random.choice(how_are_you_responses)

    # Asking for time
    elif "time" in user_input:
        current_time = datetime.now().strftime("%H:%M:%S")
        return f"The current time is {current_time}"

    # Asking for date
    elif "date" in user_input:
        current_date = datetime.now().strftime("%Y-%m-%d")
        return f"Today's date is {current_date}"

    # Tell joke
    elif "joke" in user_input:
        return random.choice(jokes)

    # Help command
    elif "help" in user_input:
        return """
You can try:
- hi
- how are you
- tell me a joke
- what is the time
- what is the date
- bye
"""

    # Exit commands
    elif user_input in ["bye", "exit", "quit"]:
        return "exit"

    # Unknown input
    else:
        return random.choice(unknown_responses)

# =========================
# Main Program Loop
# =========================

print("=" * 40)
print("🤖 Welcome to SmartBot")
print("Type 'bye' to exit.")
print("=" * 40)

while True:

    user_message = input("\nYou: ")

    response = chatbot_response(user_message)

    if response == "exit":
        print("🤖 SmartBot: Goodbye!")
        break

    print(f"🤖 SmartBot: {response}")
