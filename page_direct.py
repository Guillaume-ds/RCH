import streamlit as st

def page_direct():
    
    st.markdown(""" <iframe
    src="https://player.twitch.tv/?SypherPK&parent=streamernews.example.com"
    height="<height>"
    width="<width>"
    allowfullscreen="<allowfullscreen>">
    </iframe>""", unsafe_allow_html=True)