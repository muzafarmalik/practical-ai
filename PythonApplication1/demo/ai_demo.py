"""
=============================================================================
PRACTICAL AI DEMO - Live Demonstration Script
=============================================================================
This script demonstrates practical AI capabilities you can use TODAY.
Run each section to see AI in action.

Requirements: pip install openai textblob transformers requests
For OpenAI demos: Set your API key as environment variable OPENAI_API_KEY
=============================================================================
"""

import os
import sys

# ============================================================================
# DEMO 1: Sentiment Analysis (No API key needed!)
# ============================================================================
def demo_sentiment_analysis():
    """Analyze the emotional tone of any text - works offline!"""
    print("\n" + "="*60)
    print("🎯 DEMO 1: Sentiment Analysis (TextBlob)")
    print("="*60)

    from textblob import TextBlob

    samples = [
        "I absolutely love learning about artificial intelligence!",
        "This exam was terrible and I feel completely unprepared.",
        "The weather today is okay, nothing special.",
        "AI is revolutionizing healthcare and saving lives!",
        "I'm worried that AI might replace my future job.",
    ]

    print("\nAnalyzing sentiments of sample texts:\n")
    for text in samples:
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity  # -1 (negative) to 1 (positive)
        subjectivity = blob.sentiment.subjectivity  # 0 (objective) to 1 (subjective)

        # Visual indicator
        if polarity > 0.3:
            emoji = "😊 Positive"
        elif polarity < -0.3:
            emoji = "😟 Negative"
        else:
            emoji = "😐 Neutral"

        print(f"  \"{text[:50]}...\"")
        print(f"    → {emoji} (polarity: {polarity:.2f}, subjectivity: {subjectivity:.2f})\n")

    # Interactive part
    print("\n💡 Try it yourself!")
    user_text = input("Enter any sentence to analyze: ")
    if user_text.strip():
        result = TextBlob(user_text)
        print(f"\n  Polarity: {result.sentiment.polarity:.2f} (-1=negative, +1=positive)")
        print(f"  Subjectivity: {result.sentiment.subjectivity:.2f} (0=factual, 1=opinion)")


# ============================================================================
# DEMO 2: Text Summarization (Using Hugging Face - free, no API key!)
# ============================================================================
def demo_text_summarization():
    """Summarize long text using a pre-trained model."""
    print("\n" + "="*60)
    print("📝 DEMO 2: AI Text Summarization (Hugging Face Transformers)")
    print("="*60)

    try:
        from transformers import pipeline
    except ImportError:
        print("\n⚠️  Install transformers: pip install transformers torch")
        print("    This demo uses free, local AI models (no API key needed)")
        return

    print("\nLoading summarization model (first run downloads ~1GB)...")
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    article = """
    Artificial intelligence is transforming education in unprecedented ways.
    Students now have access to personalized tutoring systems that adapt to
    their individual learning styles and pace. AI-powered tools can identify
    knowledge gaps, suggest targeted practice materials, and provide instant
    feedback on assignments. Universities are integrating AI into curriculum
    design, using data analytics to improve student outcomes and retention
    rates. However, this transformation also raises important questions about
    academic integrity, the role of human instructors, and ensuring equitable
    access to these powerful tools across different socioeconomic backgrounds.
    The key challenge is not whether to adopt AI in education, but how to do
    so in a way that enhances rather than replaces human connection and
    critical thinking skills.
    """

    print("\n📄 Original text (150 words):")
    print(f"   {article.strip()[:200]}...")

    summary = summarizer(article, max_length=60, min_length=20, do_sample=False)

    print(f"\n✨ AI Summary ({len(summary[0]['summary_text'].split())} words):")
    print(f"   {summary[0]['summary_text']}")


# ============================================================================
# DEMO 3: AI-Powered Text Generation with OpenAI
# ============================================================================
def demo_openai_chat():
    """Demonstrate OpenAI API for practical tasks."""
    print("\n" + "="*60)
    print("🤖 DEMO 3: AI Chat Completion (OpenAI API)")
    print("="*60)

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("\n⚠️  Set OPENAI_API_KEY environment variable to run this demo.")
        print("    Example: set OPENAI_API_KEY=sk-your-key-here")
        print("\n📋 Here's what this demo does (showing the code pattern):\n")
        print("""
    from openai import OpenAI
    client = OpenAI()

    # Example: Generate a study plan
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful study assistant."},
            {"role": "user", "content": "Create a 1-week Python learning plan for beginners"}
        ],
        max_tokens=500
    )
    print(response.choices[0].message.content)
        """)
        return

    from openai import OpenAI
    client = OpenAI(api_key=api_key)

    print("\n🎓 Use Case: AI Study Assistant")
    topic = input("Enter a topic you want to learn about: ") or "Machine Learning"

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful study assistant for university students. "
                          "Give concise, practical advice."
            },
            {
                "role": "user",
                "content": f"Create a 5-step beginner's guide to learn {topic}. "
                          f"Include free resources for each step."
            }
        ],
        max_tokens=500
    )

    print(f"\n📚 Your Personalized Study Guide for '{topic}':\n")
    print(response.choices[0].message.content)


# ============================================================================
# DEMO 4: Image Description / Classification (Free - no API key)
# ============================================================================
def demo_keyword_extraction():
    """Extract keywords and topics from text using AI."""
    print("\n" + "="*60)
    print("🔑 DEMO 4: AI Keyword & Topic Extraction")
    print("="*60)

    from textblob import TextBlob

    text = """
    The rapid advancement of artificial intelligence and machine learning
    technologies is creating new opportunities in healthcare, finance, and
    education. Deep learning models are now capable of diagnosing diseases,
    predicting market trends, and personalizing educational content. Companies
    like Google, Microsoft, and OpenAI are investing billions in AI research,
    while startups are finding innovative applications in niche markets.
    """

    blob = TextBlob(text)

    print("\n📄 Input text (about AI industry):")
    print(f"   {text.strip()[:150]}...")

    # Noun phrase extraction
    print("\n🏷️  Key Topics Identified:")
    for phrase in blob.noun_phrases[:10]:
        print(f"   • {phrase}")

    # Word frequency
    print("\n📊 Most Frequent Meaningful Words:")
    word_counts = {}
    stop_words = {'the', 'is', 'in', 'and', 'of', 'are', 'a', 'to', 'that', 'for'}
    for word in blob.words.lower():
        if word not in stop_words and len(word) > 3:
            word_counts[word] = word_counts.get(word, 0) + 1

    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:8]
    for word, count in sorted_words:
        bar = "█" * (count * 3)
        print(f"   {word:20s} {bar} ({count})")


# ============================================================================
# DEMO 5: Simple Question Answering
# ============================================================================
def demo_question_answering():
    """Demonstrate AI question answering on a given context."""
    print("\n" + "="*60)
    print("❓ DEMO 5: AI Question Answering")
    print("="*60)

    try:
        from transformers import pipeline
    except ImportError:
        print("\n⚠️  Install transformers: pip install transformers torch")
        return

    print("\nLoading QA model...")
    qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

    context = """
    Python was created by Guido van Rossum and first released in 1991.
    It emphasizes code readability and simplicity. Python supports multiple
    programming paradigms including procedural, object-oriented, and functional
    programming. It has become the most popular language for artificial intelligence
    and machine learning due to libraries like TensorFlow, PyTorch, and scikit-learn.
    Python is used by companies like Google, Netflix, Instagram, and Spotify.
    """

    questions = [
        "Who created Python?",
        "When was Python first released?",
        "What is Python popular for?",
        "Which companies use Python?",
    ]

    print(f"\n📄 Context: (About Python programming language)")
    print(f"   {context.strip()[:150]}...\n")

    print("❓ Questions & AI Answers:\n")
    for q in questions:
        result = qa_pipeline(question=q, context=context)
        confidence = result['score'] * 100
        print(f"   Q: {q}")
        print(f"   A: {result['answer']} (confidence: {confidence:.1f}%)\n")


# ============================================================================
# MAIN MENU
# ============================================================================
def main():
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║         🤖 PRACTICAL AI - LIVE DEMO SUITE                  ║
    ║         Practical AI & Real-World Application               ║
    ╚══════════════════════════════════════════════════════════════╝
    """)

    demos = {
        "1": ("Sentiment Analysis (TextBlob - works offline)", demo_sentiment_analysis),
        "2": ("Text Summarization (Hugging Face - free)", demo_text_summarization),
        "3": ("AI Chat / Study Assistant (OpenAI API)", demo_openai_chat),
        "4": ("Keyword & Topic Extraction (TextBlob)", demo_keyword_extraction),
        "5": ("Question Answering (Hugging Face - free)", demo_question_answering),
        "A": ("Run ALL demos", None),
        "Q": ("Quit", None),
    }

    while True:
        print("\n" + "-"*50)
        print("Choose a demo to run:\n")
        for key, (name, _) in demos.items():
            print(f"  [{key}] {name}")

        choice = input("\nYour choice: ").strip().upper()

        if choice == "Q":
            print("\n👋 Thanks for exploring AI! Keep building! 🚀\n")
            break
        elif choice == "A":
            for key, (_, func) in demos.items():
                if func:
                    try:
                        func()
                    except Exception as e:
                        print(f"\n⚠️  Demo error: {e}")
                    print("\n" + "~"*60)
        elif choice in demos and demos[choice][1]:
            try:
                demos[choice][1]()
            except Exception as e:
                print(f"\n⚠️  Error: {e}")
                print("   Make sure you've installed requirements: pip install -r requirements.txt")
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
