"""
=============================================================================
WORKSHOP 02: Text Analysis with AI
=============================================================================
Level: Beginner to Intermediate
Time: 20-25 minutes
Goal: Learn text processing, word frequency analysis, and NLP basics

Prerequisites:
- Completed 01_getting_started.py
- Run: pip install textblob wordcloud matplotlib
- Run: python -m textblob.download_corpora
=============================================================================
"""

from textblob import TextBlob
from collections import Counter
import string

# ==========================================================================
# PART 1: Text Preprocessing (5 minutes)
# ==========================================================================

print("=" * 50)
print("🔤 PART 1: Text Preprocessing")
print("=" * 50)

# Raw text (imagine this is a customer review, essay, or article)
raw_text = """
    Artificial Intelligence (AI) is rapidly transforming how we work, learn, 
    and live. From chatbots to self-driving cars, AI applications are everywhere!
    Machine Learning, a subset of AI, enables computers to learn from data 
    without being explicitly programmed. Deep Learning, using neural networks,
    has achieved remarkable results in image recognition, natural language 
    processing, and game playing. The future of AI is incredibly exciting!!!
"""

print(f"\n📄 Raw text (length: {len(raw_text)} characters)")
print(f"   Preview: {raw_text.strip()[:80]}...")

# Step 1: Clean the text
cleaned = raw_text.strip().lower()
print(f"\n1️⃣  Lowercased: {cleaned[:80]}...")

# Step 2: Remove punctuation
cleaned_no_punct = cleaned.translate(str.maketrans('', '', string.punctuation))
print(f"2️⃣  No punctuation: {cleaned_no_punct[:80]}...")

# Step 3: Tokenize (split into words)
words = cleaned_no_punct.split()
print(f"3️⃣  Tokenized: {len(words)} words")
print(f"   First 10 words: {words[:10]}")

# Step 4: Remove stop words (common words that don't add meaning)
stop_words = {'the', 'is', 'in', 'and', 'of', 'a', 'to', 'from', 'how', 'we',
              'are', 'has', 'that', 'without', 'being', 'using', 'its', 'an',
              'for', 'with', 'on', 'at', 'by', 'this', 'it', 'as', 'or'}
meaningful_words = [w for w in words if w not in stop_words and len(w) > 2]
print(f"4️⃣  After removing stop words: {len(meaningful_words)} words")
print(f"   Meaningful words: {meaningful_words[:10]}")


# ==========================================================================
# PART 2: Word Frequency Analysis (5 minutes)
# ==========================================================================

print("\n\n" + "=" * 50)
print("📊 PART 2: Word Frequency Analysis")
print("=" * 50)

# Count word frequencies
word_freq = Counter(meaningful_words)
top_words = word_freq.most_common(10)

print("\n🏆 Top 10 Most Frequent Words:\n")
max_count = top_words[0][1] if top_words else 1
for word, count in top_words:
    bar_length = int((count / max_count) * 20)
    bar = "█" * bar_length
    print(f"   {word:20s} {bar} ({count})")

# N-grams (word combinations)
print("\n\n🔗 Common 2-Word Combinations (Bigrams):")
blob = TextBlob(raw_text.strip())
bigrams = list(blob.ngrams(n=2))[:8]
for bigram in bigrams:
    print(f"   • {' '.join(bigram)}")


# ==========================================================================
# PART 3: Named Entity & Noun Phrase Extraction (5 minutes)
# ==========================================================================

print("\n\n" + "=" * 50)
print("🏷️  PART 3: Extracting Key Topics & Phrases")
print("=" * 50)

# TextBlob noun phrase extraction
blob = TextBlob(raw_text)
noun_phrases = blob.noun_phrases

print("\n📌 Key Topics/Noun Phrases Found:\n")
for phrase in noun_phrases:
    print(f"   • {phrase}")

# Categorize by likely topic
print("\n\n🗂️  Categorized Topics:")
tech_terms = [p for p in noun_phrases if any(t in p for t in ['ai', 'learning', 'neural', 'deep'])]
app_terms = [p for p in noun_phrases if any(t in p for t in ['recognition', 'processing', 'playing', 'driving'])]

print(f"   🔬 Technology: {tech_terms}")
print(f"   📱 Applications: {app_terms}")


# ==========================================================================
# PART 4: Language Detection & Translation (5 minutes)
# ==========================================================================

print("\n\n" + "=" * 50)
print("🌍 PART 4: Language Detection")
print("=" * 50)

multilingual_texts = [
    "Hello, how are you today?",
    "Bonjour, comment allez-vous?",
    "Hola, ¿cómo estás?",
    "こんにちは、元気ですか？",
    "Hallo, wie geht es Ihnen?",
    "مرحبا، كيف حالك؟",
]

print("\n🔍 Detecting languages:\n")
for text in multilingual_texts:
    try:
        blob = TextBlob(text)
        lang = blob.detect_language()
        lang_names = {
            'en': 'English', 'fr': 'French', 'es': 'Spanish',
            'ja': 'Japanese', 'de': 'German', 'ar': 'Arabic',
            'zh-CN': 'Chinese', 'hi': 'Hindi', 'ko': 'Korean'
        }
        lang_name = lang_names.get(lang, lang)
        print(f"   \"{text}\"")
        print(f"   → Detected: {lang_name} ({lang})\n")
    except Exception:
        print(f"   \"{text}\"")
        print(f"   → (Language detection requires internet connection)\n")


# ==========================================================================
# PART 5: Practical Exercise - Analyze Your Own Text
# ==========================================================================

print("\n" + "=" * 50)
print("✏️  EXERCISE: Analyze Any Text!")
print("=" * 50)
print("""
Paste or type a paragraph (press Enter twice when done).
Suggestions: Copy a news article intro, song lyrics, or product review.
""")

lines = []
print("Enter text (press Enter on empty line to finish):")
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

user_text = " ".join(lines)

if user_text.strip():
    print("\n" + "-" * 40)
    print("📊 YOUR TEXT ANALYSIS RESULTS")
    print("-" * 40)

    blob = TextBlob(user_text)

    # Basic stats
    print(f"\n📏 Basic Statistics:")
    print(f"   Characters: {len(user_text)}")
    print(f"   Words: {len(blob.words)}")
    print(f"   Sentences: {len(blob.sentences)}")

    # Sentiment
    print(f"\n🎭 Sentiment:")
    print(f"   Polarity: {blob.sentiment.polarity:.2f} (-1 to +1)")
    print(f"   Subjectivity: {blob.sentiment.subjectivity:.2f} (0=fact, 1=opinion)")

    # Key phrases
    print(f"\n🏷️  Key Phrases:")
    for phrase in blob.noun_phrases[:5]:
        print(f"   • {phrase}")

    # Top words
    user_words = [w.lower() for w in blob.words if w.lower() not in stop_words and len(w) > 2]
    user_freq = Counter(user_words).most_common(5)
    print(f"\n📈 Top Words:")
    for word, count in user_freq:
        print(f"   • {word} ({count}x)")
else:
    print("   (No text entered - that's okay! Try again later.)")


# ==========================================================================
# WRAP UP
# ==========================================================================
print("\n\n" + "=" * 50)
print("🎉 WORKSHOP 02 COMPLETE!")
print("=" * 50)
print("""
You learned:
  ✅ Text preprocessing (cleaning, tokenizing, removing stop words)
  ✅ Word frequency analysis and visualization
  ✅ Noun phrase and topic extraction
  ✅ Language detection
  ✅ Building a complete text analysis pipeline

Challenge ideas:
  🏆 Analyze tweets about a trending topic
  🏆 Compare sentiment of different news sources
  🏆 Build a "reading level" analyzer for documents
  🏆 Create a keyword extractor for your resume/CV

Next: → 03_build_chatbot.py (Build your own chatbot!)
""")
