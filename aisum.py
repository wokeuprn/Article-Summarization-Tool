import streamlit as st
import transformers
from transformers import pipeline

# Starting Streamlit command
st.set_page_config(page_title="Article Summarizer", layout="centered")

# Load the summarizer model once
@st.cache_resource
def load_summarizer():
    return pipeline("summarization", model="facebook/bart-large-cnn")

summarizer = load_summarizer()

# Streamlit patching
st.title("📝 Article Summarizer using NLP")
st.write("Paste a long paragraph or article below and click **Summarize** to get a concise version.")
st.write("Word count of 10000 words.")

# Text input area
input_text = st.text_area("Enter your text here:", height=250)

# Button to trigger summarization
if st.button("Summarize"):
    if len(input_text.strip()) < 50:
        st.warning("Please enter a longer paragraph (at least 50 characters).")
    else:
        with st.spinner("Summarizing..."):
            summary = summarizer(input_text, max_length=10000, min_length=30, do_sample=False)
            st.subheader("Summary:")
            st.success(summary[0]['summary_text'])
