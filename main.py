from datetime import datetime, timedelta, timezone
import datetime
import random

# ------------------ Command Handlers ------------------ #

def handle_greeting():
    print("Jack: Hello! How can I assist you today?")

def handle_name():
    print("Jack: You can call me Jack – your virtual assistant!")

def handle_python_info():
    print("Jack: Python is a high-level, interpreted programming language known for its simplicity and readability.\n"
          "It's widely used in web development, data science, automation, AI, and more!")

def handle_fact():
    facts = [
        "The first computer programmer was Ada Lovelace in the 1800s.",
        "Python was named after the comedy group Monty Python, not the snake.",
        "Git was created by Linus Torvalds, the same person who made Linux.",
        "The first ever computer virus was created in 1986 and was called Brain.",
        "There are over 700 programming languages in the world!"
    ]
    print("Jack 💡:", random.choice(facts))

def handle_tip():
    tips = [
        "Use list comprehensions for cleaner, faster loops in Python.",
        "Break your code into functions for better readability and reuse.",
        "Always use version control like Git when working on projects.",
        "Comment your code — your future self will thank you!",
        "Use virtual environments to manage project dependencies."
    ]
    print("Jack 🧠:", random.choice(tips))

def handle_quote():
    quotes = [
        '"Programs must be written for people to read, and only incidentally for machines to execute." – Harold Abelson',
        '"Talk is cheap. Show me the code." – Linus Torvalds',
        '"The best error message is the one that never shows up." – Thomas Fuchs',
        '"Simplicity is the soul of efficiency." – Austin Freeman',
        '"Code is like humor. When you have to explain it, it’s bad." – Cory House'
    ]
    print("Jack 🧾:", random.choice(quotes))

    print("Jack 🧾:", random.choice(quotes))

def handle_joke():
    jokes = [
        "Why did the Python programmer go hungry? Because his food was in a tuple!",
        "Why do Java developers wear glasses? Because they don’t C#.",
        "What do you call 8 hobbits? A hobbyte.",
        "Why was the developer unhappy at their job? They wanted arrays!",
    ]
    print("Jack 🤖:", random.choice(jokes))

def handle_time():
    now_utc = datetime.now(timezone.utc)
    ist_offset = timedelta(hours=5, minutes=30)
    now_ist = now_utc.astimezone(timezone(ist_offset))
    time_str = now_ist.strftime("%I:%M %p").lstrip("0")
    print(f"Jack: It's currently {time_str}.")

def handle_date():
    today = datetime.date.today()
    date_str = today.strftime("%A, %B %d, %Y")
    print(f"Jack: Today is {date_str}.")

def handle_math():
    expr = input("Jack 🔢: Please enter a math expression (e.g., 8 * (3 + 2)):\nYou: ")
    try:
        result = eval(expr, {"__builtins__": {}}, {})
        print("Jack: The result is", result)
    except Exception:
        print("Jack: Hmm, that doesn’t look like valid math. Try again!")

def handle_help():
    print("""
📌 Jack can help you with the following commands:
- greeting      → Say hello
- name          → Ask Jack's name
- python        → Get basic info about Python
- fact          → Hear a random programming fact
- tip           → Get a useful coding tip
- quote         → See an inspirational tech quote
- joke          → Hear a tech-related joke
- time          → Get the current time
- date          → Find out today's date
- math          → Calculate a math expression
- help          → Show this menu
- stop / exit   → Quit the assistant
    """)

# ------------------ Command Registry ------------------ #

COMMANDS = {
    "greeting": handle_greeting,
    "hello": handle_greeting,
    "hi": handle_greeting,
    "name": handle_name,
    "who are you": handle_name,
    "python": handle_python_info,
    "fact": handle_fact,
    "tip": handle_tip,
    "quote": handle_quote,
    "joke": handle_joke,
    "funny": handle_joke,
    "time": handle_time,
    "clock": handle_time,
    "date": handle_date,
    "today": handle_date,
    "math": handle_math,
    "calculate": handle_math,
    "help": handle_help
}

# ------------------ Main Loop ------------------ #

def main():
    print("=" * 40)
    print("🤖 Welcome to Jack – Your Professional Python Assistant")
    print("=" * 40)
    print("Type 'help' to see what I can do. Type 'exit' or 'stop' to quit.\n")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input in ["exit", "stop", "quit", "bye"]:
            print("Jack: Goodbye! 👋 Stay curious and keep coding.")
            break

        matched = False
        for key in COMMANDS:
            if key in user_input:
                COMMANDS[key]()
                matched = True
                break

        if not matched:
            print("Jack: Hmm... I didn’t catch that. Type 'help' to see available commands.")

if __name__ == "__main__":
    main()
