"""
=============================================================================
WORKSHOP 03: Build a Simple Chatbot
=============================================================================
Level: Beginner to Intermediate
Time: 25-30 minutes
Goal: Build 3 progressively smarter chatbots

Prerequisites:
- Completed 01 and 02 workshops
- Run: pip install textblob
- Optional: pip install openai (for Part 3 - needs API key)
=============================================================================
"""

import random
import datetime

# ==========================================================================
# PART 1: Rule-Based Chatbot (10 minutes)
# ==========================================================================

print("=" * 50)
print("🤖 PART 1: Rule-Based Chatbot")
print("=" * 50)
print("""
This is the simplest type of chatbot - it uses IF/ELSE rules
to match user input to pre-written responses.
Think: early customer service bots, FAQ bots.
""")


def rule_based_chatbot(user_input):
    """A simple rule-based chatbot using keyword matching."""
    user_input = user_input.lower().strip()

    # Greeting patterns
    if any(word in user_input for word in ['hello', 'hi', 'hey', 'greetings']):
        responses = [
            "Hello! How can I help you today? 👋",
            "Hey there! What's on your mind?",
            "Hi! Great to chat with you!"
        ]
        return random.choice(responses)

    # Questions about AI
    elif any(word in user_input for word in ['what is ai', 'artificial intelligence', 'define ai']):
        return ("AI (Artificial Intelligence) is the simulation of human intelligence "
                "by machines. It includes learning, reasoning, and self-correction. "
                "Think of it as teaching computers to think! 🧠")

    # Questions about learning
    elif any(word in user_input for word in ['learn', 'start', 'begin', 'how to']):
        return ("Great question! Here's how to start:\n"
                "  1. Learn Python basics (free on Codecademy)\n"
                "  2. Try Google Colab for free coding\n"
                "  3. Take Andrew Ng's ML course on Coursera\n"
                "  4. Build small projects and share them! 🚀")

    # Questions about tools
    elif any(word in user_input for word in ['tool', 'recommend', 'best', 'use']):
        return ("Here are my top AI tool recommendations:\n"
                "  📝 Writing: ChatGPT, Claude, Grammarly\n"
                "  💻 Coding: GitHub Copilot, Cursor\n"
                "  🎨 Creative: Midjourney, Canva AI\n"
                "  📊 Data: Google Colab, Kaggle")

    # Questions about careers
    elif any(word in user_input for word in ['job', 'career', 'work', 'salary']):
        return ("AI careers are booming! Top roles:\n"
                "  • ML Engineer ($130-200K)\n"
                "  • Data Scientist ($100-160K)\n"
                "  • AI Product Manager ($120-180K)\n"
                "  • AI Ethics Specialist ($90-140K)\n"
                "  Start building projects NOW - portfolio > degree! 💼")

    # Feelings/emotions
    elif any(word in user_input for word in ['feel', 'scared', 'worried', 'anxious', 'excited']):
        return ("It's totally normal to have mixed feelings about AI! 💛\n"
                "Remember: AI is a TOOL, not a replacement for human creativity.\n"
                "The best approach? Stay curious and keep learning!")

    # Goodbye
    elif any(word in user_input for word in ['bye', 'quit', 'exit', 'goodbye']):
        return "GOODBYE"

    # Time
    elif any(word in user_input for word in ['time', 'date', 'today']):
        now = datetime.datetime.now()
        return f"It's {now.strftime('%A, %B %d, %Y at %I:%M %p')} ⏰"

    # Default fallback
    else:
        fallbacks = [
            "Interesting! Could you tell me more about that?",
            "I'm not sure I understand. Try asking about AI, tools, or careers!",
            "Hmm, let me think... Can you rephrase that?",
            "That's a great point! What else would you like to know about AI?"
        ]
        return random.choice(fallbacks)


# Run the rule-based chatbot
print("💬 Chat with RuleBot (type 'bye' to exit):\n")
print("   Try asking: 'What is AI?', 'How do I start?', 'What tools should I use?'\n")

while True:
    user_msg = input("You: ")
    if not user_msg.strip():
        continue
    response = rule_based_chatbot(user_msg)
    if response == "GOODBYE":
        print("Bot: Goodbye! Keep learning! 👋🚀\n")
        break
    print(f"Bot: {response}\n")


# ==========================================================================
# PART 2: Smarter Bot with Sentiment Awareness (10 minutes)
# ==========================================================================

print("\n" + "=" * 50)
print("🧠 PART 2: Sentiment-Aware Chatbot")
print("=" * 50)
print("""
This bot understands your MOOD and responds accordingly.
It combines rule-based responses with sentiment analysis.
""")

try:
    from textblob import TextBlob

    class SmartChatbot:
        """A chatbot that understands user sentiment and adapts responses."""

        def __init__(self, name="SmartBot"):
            self.name = name
            self.conversation_history = []
            self.mood_score = 0  # Track overall conversation mood

        def analyze_mood(self, text):
            """Analyze the sentiment of user input."""
            blob = TextBlob(text)
            return blob.sentiment.polarity, blob.sentiment.subjectivity

        def get_response(self, user_input):
            """Generate a response based on content AND mood."""
            polarity, subjectivity = self.analyze_mood(user_input)
            self.mood_score = (self.mood_score + polarity) / 2  # Rolling average

            # Store in history
            self.conversation_history.append({
                "user": user_input,
                "sentiment": polarity
            })

            user_lower = user_input.lower()

            # Mood-aware responses
            if polarity < -0.5:
                # Very negative - be supportive
                prefix = random.choice([
                    "I can sense some frustration. ",
                    "That sounds challenging. ",
                    "I hear you - that's tough. "
                ])
            elif polarity > 0.5:
                # Very positive - be enthusiastic
                prefix = random.choice([
                    "Love the energy! 🔥 ",
                    "That's awesome to hear! ",
                    "Your enthusiasm is contagious! "
                ])
            else:
                prefix = ""

            # Content-based response
            if any(w in user_lower for w in ['help', 'stuck', 'confused']):
                content = ("No worries! Here's what I suggest:\n"
                          "  1. Break the problem into smaller pieces\n"
                          "  2. Search for similar examples online\n"
                          "  3. Ask an AI assistant for explanation\n"
                          "  4. Take a break and come back fresh!")
            elif any(w in user_lower for w in ['project', 'build', 'create', 'make']):
                content = ("Building projects is the BEST way to learn! Ideas:\n"
                          "  🎯 Personal AI assistant (using OpenAI API)\n"
                          "  🎯 Sentiment tracker for social media\n"
                          "  🎯 Study scheduler with AI recommendations\n"
                          "  🎯 Resume optimizer using NLP")
            elif any(w in user_lower for w in ['bye', 'quit', 'exit']):
                return "GOODBYE"
            else:
                content = rule_based_chatbot(user_input)
                if content == "GOODBYE":
                    return "GOODBYE"

            # Add mood indicator
            mood_indicator = f"\n   [Mood detected: {'😊' if polarity > 0.2 else '😟' if polarity < -0.2 else '😐'} ({polarity:.2f})]"

            return prefix + content + mood_indicator

        def get_summary(self):
            """Summarize the conversation."""
            if not self.conversation_history:
                return "No conversation yet!"
            avg_sentiment = sum(h['sentiment'] for h in self.conversation_history) / len(self.conversation_history)
            return (f"\n📊 Conversation Summary:\n"
                    f"   Messages exchanged: {len(self.conversation_history)}\n"
                    f"   Average mood: {avg_sentiment:.2f}\n"
                    f"   Overall vibe: {'Positive 😊' if avg_sentiment > 0.1 else 'Negative 😟' if avg_sentiment < -0.1 else 'Neutral 😐'}")

    # Run the smart chatbot
    bot = SmartChatbot("SmartBot")
    print(f"\n💬 Chat with {bot.name} (type 'bye' to exit):\n")
    print("   This bot detects your mood! Try positive and negative messages.\n")

    while True:
        user_msg = input("You: ")
        if not user_msg.strip():
            continue
        response = bot.get_response(user_msg)
        if response == "GOODBYE":
            print(f"Bot: Thanks for chatting! 👋")
            print(bot.get_summary())
            break
        print(f"Bot: {response}\n")

except ImportError:
    print("⚠️  Install TextBlob: pip install textblob")


# ==========================================================================
# PART 3: AI-Powered Chatbot with OpenAI (10 minutes)
# ==========================================================================

print("\n\n" + "=" * 50)
print("🚀 PART 3: AI-Powered Chatbot (OpenAI)")
print("=" * 50)

import os

api_key = os.environ.get("OPENAI_API_KEY")

if not api_key:
    print("""
⚠️  This section requires an OpenAI API key.
   Set it: set OPENAI_API_KEY=sk-your-key-here

📋 Here's the code pattern (study it even without a key):
""")
    print("""
    from openai import OpenAI

    client = OpenAI()

    # System message defines the bot's personality
    messages = [
        {"role": "system", "content": 
            "You are a friendly AI tutor helping university students "
            "learn about artificial intelligence. Be encouraging, "
            "give practical examples, and suggest hands-on exercises."}
    ]

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['bye', 'quit', 'exit']:
            break

        # Add user message to conversation
        messages.append({"role": "user", "content": user_input})

        # Get AI response
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Fast and affordable
            messages=messages,
            max_tokens=300,
            temperature=0.7  # Creativity level (0=focused, 1=creative)
        )

        # Extract and display response
        bot_reply = response.choices[0].message.content
        messages.append({"role": "assistant", "content": bot_reply})

        print(f"AI Tutor: {bot_reply}")
    """)
    print("""
💡 Key Concepts:
   • "messages" list maintains conversation history (context)
   • "system" message = bot's personality/instructions
   • "temperature" controls randomness (0=deterministic, 1=creative)
   • "max_tokens" limits response length (saves money)
   • Each API call costs ~$0.001 with gpt-4o-mini
""")
else:
    from openai import OpenAI

    client = OpenAI(api_key=api_key)

    messages = [
        {"role": "system", "content":
            "You are a friendly AI tutor helping university students "
            "learn about artificial intelligence and technology. Be encouraging, "
            "give practical examples, and suggest hands-on exercises. "
            "Keep responses concise (under 150 words)."}
    ]

    print("\n💬 Chat with AI Tutor (powered by GPT-4o-mini)")
    print("   Type 'bye' to exit\n")

    while True:
        user_input = input("You: ")
        if not user_input.strip():
            continue
        if user_input.lower().strip() in ['bye', 'quit', 'exit']:
            print("AI Tutor: Keep building amazing things! See you next time! 🚀")
            break

        messages.append({"role": "user", "content": user_input})

        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages,
                max_tokens=300,
                temperature=0.7
            )
            bot_reply = response.choices[0].message.content
            messages.append({"role": "assistant", "content": bot_reply})
            print(f"AI Tutor: {bot_reply}\n")
        except Exception as e:
            print(f"⚠️  Error: {e}\n")


# ==========================================================================
# WRAP UP & CHALLENGE
# ==========================================================================
print("\n\n" + "=" * 50)
print("🎉 WORKSHOP 03 COMPLETE!")
print("=" * 50)
print("""
You built THREE chatbots:
  ✅ Rule-Based Bot (keyword matching, simple but effective)
  ✅ Sentiment-Aware Bot (understands user emotions)
  ✅ AI-Powered Bot (using large language models via API)

🏆 CHALLENGES to level up:

  1. EASY: Add more rules to the rule-based bot
     (weather, jokes, fun facts)

  2. MEDIUM: Make the sentiment bot remember user preferences
     and personalize responses over time

  3. HARD: Build a "study buddy" bot that:
     - Takes a topic from the user
     - Generates quiz questions
     - Tracks correct/incorrect answers
     - Adjusts difficulty based on performance

  4. EXPERT: Deploy your bot as a web app using:
     - Flask or Streamlit for the frontend
     - OpenAI API for intelligence
     - Deploy free on Render or Streamlit Cloud

📚 Resources:
  • OpenAI API docs: https://platform.openai.com/docs
  • Streamlit: https://streamlit.io
  • Flask tutorial: https://flask.palletsprojects.com
  • LangChain (advanced): https://langchain.com
""")
