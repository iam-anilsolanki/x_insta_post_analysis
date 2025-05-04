import streamlit as st
import requests
from PIL import Image
from io import BytesIO
from textblob import TextBlob
import snscrape.modules.twitter as sntwitter
import instaloader

# --------- Functions ---------

def get_twitter_data(url):
    try:
        tweet_id = url.split('/')[-1]
        tweet = next(sntwitter.TwitterTweetScraper(tweet_id).get_items())
        text = tweet.content
        img_url = tweet.media[0].fullUrl if tweet.media else None
        return text, img_url
    except Exception as e:
        return None, None

def get_instagram_data(url):
    try:
        L = instaloader.Instaloader()
        shortcode = url.strip('/').split('/')[-1]
        post = instaloader.Post.from_shortcode(L.context, shortcode)
        return post.caption, post.url
    except Exception as e:
        return None, None

def download_image(img_url):
    response = requests.get(img_url)
    return Image.open(BytesIO(response.content))

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.1:
        return "Positive 😊"
    elif polarity < -0.1:
        return "Negative 😞"
    else:
        return "Neutral 😐"

# --------- Streamlit UI ---------

st.set_page_config(page_title="Social Media Post Sentiment Analyzer", layout="centered")
st.title("🧠 Social Media Post Sentiment Analyzer")
st.markdown("Enter a **Twitter** or **Instagram** post URL below:")

url = st.text_input("Paste post URL here")

if st.button("Analyze"):
    if "twitter.com" in url:
        caption, img_url = get_twitter_data(url)
    elif "instagram.com" in url:
        caption, img_url = get_instagram_data(url)
    else:
        st.error("Unsupported URL. Please use Twitter or Instagram.")
        st.stop()

    if caption:
        st.markdown(f"### 📝 Caption:\n> {caption}")
        sentiment = analyze_sentiment(caption)
        st.markdown(f"### 🔍 Caption Sentiment: **{sentiment}**")

        if img_url:
            image = download_image(img_url)
            st.image(image, caption="Post Image", use_column_width=True)
    else:
        st.error("Could not retrieve post data. Make sure the post is public.")

