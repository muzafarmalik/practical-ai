# 🤖 Practical AI Workshop - Hands-On Learning

## Overview

This workshop accompanies the **"Practical AI & Real-World Application"** guest lecture. It provides hands-on coding exercises that take you from zero to building AI-powered applications.

**Audience:** University/College students (undergraduate & graduate)  
**Time Required:** 60-90 minutes (self-paced)  
**Difficulty:** Beginner → Intermediate

---

## 📁 Project Structure

```
├── presentation/
│   └── index.html          # Interactive Reveal.js slide deck (open in browser)
│
├── demo/
│   ├── ai_demo.py          # Live demo script (5 AI demos with menu)
│   └── requirements.txt    # Dependencies for demos
│
└── workshop/
	├── 01_getting_started.py   # Python basics + first AI script
	├── 02_text_analysis.py     # NLP, text processing, word analysis
	├── 03_build_chatbot.py     # Build 3 chatbots (rule → AI-powered)
	└── README.md               # This file
```

---

## 🚀 Quick Start

### Option A: Google Colab (No Installation - Recommended for Beginners)

1. Go to [Google Colab](https://colab.research.google.com)
2. Create a new notebook
3. Copy-paste code from each workshop file into cells
4. Run cells with `Shift + Enter`

### Option B: Local Setup

#### Prerequisites
- Python 3.9+ installed ([Download Python](https://www.python.org/downloads/))
- A code editor (VS Code, PyCharm, or any text editor)

#### Installation Steps

```bash
# 1. Clone or download this repository
# 2. Open terminal in the project folder

# 3. Create a virtual environment (recommended)
python -m venv ai_workshop
# Windows:
ai_workshop\Scripts\activate
# Mac/Linux:
source ai_workshop/bin/activate

# 4. Install dependencies
pip install textblob transformers torch openai requests

# 5. Download TextBlob language data
python -m textblob.download_corpora

# 6. Run the first workshop!
python workshop/01_getting_started.py
```

---

## 📋 Workshop Progression

| # | Script | What You'll Learn | Time |
|---|--------|-------------------|------|
| 1 | `01_getting_started.py` | Python basics, sentiment analysis | 15-20 min |
| 2 | `02_text_analysis.py` | NLP, word frequency, topic extraction | 20-25 min |
| 3 | `03_build_chatbot.py` | Build 3 chatbots (simple → AI-powered) | 25-30 min |

---

## 🛠️ Tools & Libraries Used

| Library | Purpose | Cost |
|---------|---------|------|
| TextBlob | Sentiment analysis, NLP basics | Free |
| Transformers | Hugging Face AI models | Free |
| OpenAI | GPT-4o-mini API access | ~$0.001/request |

---

## 🔑 OpenAI API Setup (Optional)

Some demos use the OpenAI API. To set it up:

1. Create an account at [platform.openai.com](https://platform.openai.com)
2. Generate an API key in Settings → API Keys
3. Set the environment variable:

```bash
# Windows (Command Prompt)
set OPENAI_API_KEY=sk-your-key-here

# Windows (PowerShell)
$env:OPENAI_API_KEY="sk-your-key-here"

# Mac/Linux
export OPENAI_API_KEY=sk-your-key-here
```

**Note:** Most workshop exercises work WITHOUT an API key using free local models!

---

## 🎯 Presentation (Slides)

Open the interactive presentation in any web browser:

```bash
# Simply open the file:
presentation/index.html

# Or start a local server for best experience:
python -m http.server 8000 --directory presentation
# Then visit: http://localhost:8000
```

**Keyboard shortcuts:**
- `→` / `←` — Navigate slides
- `↓` / `↑` — Navigate vertical slides (sub-sections)
- `S` — Open speaker notes
- `F` — Fullscreen
- `O` — Overview mode
- `B` — Blackout (pause)

---

## 🏆 After the Workshop - Next Steps

### Keep Learning (Free Resources)
- [fast.ai](https://www.fast.ai/) — Practical Deep Learning for Coders
- [Andrew Ng's ML Course](https://www.coursera.org/learn/machine-learning) — Coursera
- [Google AI Essentials](https://grow.google/ai-essentials/) — Google Career Certificates
- [Microsoft AI Skills](https://learn.microsoft.com/en-us/ai/) — Microsoft Learn

### Practice Platforms
- [Kaggle](https://www.kaggle.com/) — Datasets, competitions, free notebooks
- [Hugging Face](https://huggingface.co/) — Models, datasets, spaces
- [Google Colab](https://colab.research.google.com) — Free GPU for ML experiments
- [Replit](https://replit.com/) — Code and deploy in-browser

### Build Projects
- Personal AI assistant / chatbot
- Sentiment analysis dashboard
- AI-powered study planner
- Image classifier for your hobby
- Text summarizer for lectures

### Get Certified
- AWS AI Practitioner
- Google Cloud AI Fundamentals
- Azure AI Fundamentals (AI-900)
- IBM AI Engineering Certificate

---

## ❓ Troubleshooting

| Problem | Solution |
|---------|----------|
| `ModuleNotFoundError` | Run `pip install <module_name>` |
| TextBlob corpora error | Run `python -m textblob.download_corpora` |
| OpenAI API error | Check your API key is set correctly |
| Transformers slow first run | First download takes a few minutes (models are large) |
| Python not found | Install Python from python.org and add to PATH |

---

## 📬 Contact

**Speaker:** Muzafar Hussain 
**Email:** muzafadev786@gmail.com
**LinkedIn:** https://www.linkedin.com/in/muzafarmalik
**GitHub:** https://github.com/muzafarmalik

---

*Built for the "Practical AI & Real-World Application" guest lecture*  
*Feel free to fork, modify, and share with attribution! 🚀*
