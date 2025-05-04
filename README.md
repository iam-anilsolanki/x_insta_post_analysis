🧠 Social Media Post Sentiment Analyzer
A simple Streamlit-based web app that takes a Twitter or Instagram post URL, extracts the caption and image, and performs sentiment analysis to tell you whether the post is Positive, Negative, or Neutral.

<br/>


🔍 Features
✅ Paste any public Twitter or Instagram post URL

📝 Extracts caption text

🖼️ Downloads and shows the post image

📊 Performs sentiment analysis on the caption using TextBlob

🧼 Clean and responsive Streamlit UI

☁️ Ready to deploy on Streamlit Cloud

🚀 Demo
Try it live here (if deployed):
Streamlit App URL

🛠️ Tech Stack
Python 3

Streamlit (for web UI)

TextBlob (for sentiment analysis)

snscrape (for Twitter post data)

Instaloader (for Instagram post data)

Pillow and requests (for image handling)

📦 Setup Instructions
bash
Copy
Edit
git clone https://github.com/yourusername/social-sentiment-analyzer.git
cd social-sentiment-analyzer

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows

pip install -r requirements.txt
streamlit run app.py
📁 File Structure
bash
Copy
Edit
social-sentiment-analyzer/
│
├── app.py                # Main Streamlit app
├── requirements.txt      # Required Python packages
└── README.md             # Project description
🌐 How It Works
User enters a Twitter or Instagram post URL

App extracts:

Caption (text)

First image from the post (if available)

Sentiment analysis is done on the caption

Image and sentiment result are shown to the user

⚠️ Limitations
Only works with public Instagram/Twitter posts

Instagram scraping may fail if the post is private or account is restricted

No login-based scraping (for ethical and legal reasons)

📄 License
This project is licensed under the MIT License – feel free to use and modify.

✨ Contributions
Contributions are welcome! Please feel free to open issues or submit PRs.
