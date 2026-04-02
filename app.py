import streamlit as st
from model import predict_url
st.set_page_config(page_title="Phishing Website Analyzer", page_icon="🔐")
st.title("🔐 Phishing Website Analyzer")
st.write("Enter a URL to check whether it is safe or phishing.")
url = st.text_input("Enter Website URL")
if st.button("check"):
    if not url:
        st.warning("Please enter a URL")
    else:
        result = predict_url(url)
        if result == 1:
            st.error("⚠️ Phishing Website Detected!")
        else:
            st.success("✅ Safe Website")