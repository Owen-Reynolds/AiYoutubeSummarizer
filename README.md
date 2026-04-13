# YouTube AI Summarizer 🤖📺

A sleek, modern desktop application that generates intelligent summaries of YouTube videos using OpenAI's GPT-4o-mini. Simply paste a link, choose a mood, and get a concise summary in seconds.

## ✨ Features

- **AI-Powered Summarization**: Uses GPT-4o-mini to analyze video transcripts and provide high-quality summaries.
- **Mood Selection**: Customize the tone of your summary (e.g., Professional, Funny, Sarcastic, etc.).
- **Real-time Streaming**: Watch the AI generate the summary token-by-token.
- **Modern UI**: A premium dark-themed interface built with Tkinter (Catppuccin Macchiato style).
- **Video ID Detection**: Automatically extracts video IDs from both standard and shortened YouTube URLs.

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- An OpenAI API Key

### Installation

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd AiYoutubeSummarizer
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Mac/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the root directory and add your OpenAI API key:
   ```env
   OPENAI_API_KEY=your_actual_api_key_here
   ```

## 🛠️ Usage

Simply run the application:
```bash
python app.py
```

1. Paste a YouTube URL in the input field.
2. Select your desired **Mood** from the listbox.
3. Click **Summarize**.
4. Read the summary, key points, and verdict in the result box.

## 📦 Tech Stack

- **Frontend**: Python Tkinter
- **AI Model**: OpenAI GPT-4o-mini
- **Data Source**: `youtube-transcript-api`
- **Configuration**: `python-dotenv`

## 📄 License

[MIT](LICENSE) - Feel free to use and modify for your own projects!
