"""
=============================================================================
WORKSHOP 01: Getting Started with AI in Python
=============================================================================
Level: Complete Beginner
Time: 15-20 minutes
Goal: Understand basic Python concepts and make your first AI-powered script

Prerequisites:
- Python installed (or use Google Colab: https://colab.research.google.com)
- Run: pip install textblob
- Run: python -m textblob.download_corpora
=============================================================================
"""

# ==========================================================================
# PART 1: Python Basics Refresher (5 minutes)
# ==========================================================================

print("=" * 50)
print("🐍 PART 1: Python Basics")
print("=" * 50)

# Variables - storing information
name = "AI Workshop Student"
year = 2025
is_excited = True

print(f"\nHello, {name}!")
print(f"Welcome to the {year} AI Workshop!")
print(f"Excited to learn? {is_excited}")

# Lists - storing collections
ai_tools = ["ChatGPT", "GitHub Copilot", "Midjourney", "Claude", "Gemini"]
print(f"\nPopular AI tools: {ai_tools}")
print(f"Number of tools: {len(ai_tools)}")
print(f"First tool: {ai_tools[0]}")

# Loops - repeating actions
print("\n🔄 Let's loop through our tools:")
for i, tool in enumerate(ai_tools, 1):
    print(f"   {i}. {tool}")

# Functions - reusable code blocks
def greet_student(student_name, major="Computer Science"):
    """A simple function to greet a student."""
    return f"👋 Welcome {student_name}! Great to have a {major} student here!"

print("\n" + greet_student("Alex", "Biology"))
print(greet_student("Sam", "Business"))
print(greet_student("Jordan"))  # Uses default major


# ==========================================================================
# PART 2: Working with Text Data (5 minutes)
# ==========================================================================

print("\n\n" + "=" * 50)
print("📝 PART 2: Working with Text Data")
print("=" * 50)

# String manipulation
sentence = "Artificial Intelligence is changing the world!"
print(f"\nOriginal: {sentence}")
print(f"Uppercase: {sentence.upper()}")
print(f"Word count: {len(sentence.split())}")
print(f"Contains 'AI': {'AI' in sentence or 'Intelligence' in sentence}")

# Dictionaries - key-value pairs (like a mini database)
student_data = {
    "name": "Workshop Student",
    "skills": ["Python", "Data Analysis"],
    "ai_experience": "beginner",
    "goals": "Build an AI-powered app"
}

print(f"\n📊 Student Profile:")
for key, value in student_data.items():
    print(f"   {key}: {value}")

# Adding new skills
student_data["skills"].append("AI Basics")
print(f"\n✅ Updated skills: {student_data['skills']}")


# ==========================================================================
# PART 3: Your First AI - Sentiment Analysis (5 minutes)
# ==========================================================================

print("\n\n" + "=" * 50)
print("🤖 PART 3: Your First AI Script!")
print("=" * 50)

try:
    from textblob import TextBlob

    # Analyze sentiment of text
    texts = [
        "I love learning new things about technology!",
        "This homework is so frustrating and difficult.",
        "The lecture was okay, nothing special happened.",
        "AI is incredible and I can't wait to build something!",
    ]

    print("\n🎭 Sentiment Analysis Results:\n")
    for text in texts:
        analysis = TextBlob(text)
        score = analysis.sentiment.polarity

        # Convert score to emoji
        if score > 0.3:
            mood = "😊 Positive"
        elif score < -0.3:
            mood = "😟 Negative"
        else:
            mood = "😐 Neutral"

        print(f"   \"{text}\"")
        print(f"   → Score: {score:.2f} | Mood: {mood}\n")

    # ==========================================================================
    # EXERCISE: Try it yourself!
    # ==========================================================================
    print("\n" + "=" * 50)
    print("✏️  EXERCISE: Analyze Your Own Text!")
    print("=" * 50)
    print("\nType a sentence and press Enter (or press Enter to skip):")

    user_input = input("> ")
    if user_input.strip():
        result = TextBlob(user_input)
        print(f"\n   Your text: \"{user_input}\"")
        print(f"   Polarity:    {result.sentiment.polarity:.2f} (range: -1 to +1)")
        print(f"   Subjectivity: {result.sentiment.subjectivity:.2f} (0=fact, 1=opinion)")

        if result.sentiment.polarity > 0:
            print("   🎉 That sounds positive!")
        elif result.sentiment.polarity < 0:
            print("   💪 That sounds tough, but you've got this!")
        else:
            print("   🤔 That's pretty neutral!")

except ImportError:
    print("\n⚠️  TextBlob not installed!")
    print("   Run: pip install textblob")
    print("   Then: python -m textblob.download_corpora")


# ==========================================================================
# WRAP UP
# ==========================================================================
print("\n\n" + "=" * 50)
print("🎉 CONGRATULATIONS!")
print("=" * 50)
print("""
You just:
  ✅ Reviewed Python basics (variables, loops, functions)
  ✅ Worked with text data and dictionaries
  ✅ Built your first AI-powered sentiment analyzer!

Next steps:
  → Move to 02_text_analysis.py for more AI text processing
  → Move to 03_build_chatbot.py to build your own chatbot
  → Try modifying this script - what else can you analyze?
""")
