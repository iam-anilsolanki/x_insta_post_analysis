import streamlit as st
import instaloader
from PIL import Image
from io import BytesIO
from textblob import TextBlob

# Instagram Profile Scraping Function
def scrape_instagram_profile(username):
    L = instaloader.Instaloader()
    try:
        # Load the profile
        profile = instaloader.Profile.from_username(L.context, username)
        # Extract basic details
        details = {
            "Username": profile.username,
            "Full Name": profile.full_name,
            "Followers": profile.followers,
            "Following": profile.followees,
            "Posts": profile.mediacount
        }
        # Display profile details
        return details
    except Exception as e:
        st.error(f"Error fetching data for {username}: {str(e)}")
        return None

# Sentiment Analysis Function
def analyze_sentiment(caption):
    blob = TextBlob(caption)
    sentiment = blob.sentiment.polarity
    return sentiment

# Streamlit Interface
st.title("Instagram Post Analysis")

# Input for Instagram username
username = st.text_input("Enter Instagram Username:", "")
if username:
    # Scrape profile data
    profile_details = scrape_instagram_profile(username)
    if profile_details:
        st.write(profile_details)

    # Display images and analyze sentiment for each post
    L = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(L.context, username)
    for post in profile.get_posts():
        st.image(post.url, caption=post.caption[:100], use_column_width=True)
        sentiment = analyze_sentiment(post.caption)
        st.write(f"Sentiment Score: {sentiment}")
