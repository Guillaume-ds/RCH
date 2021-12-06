import streamlit as st

from streamlit_player import st_player

def page_direct():
    
    link = st.text_input(label= "Link of the video")
    play = st.button("play the video")
    if play:
        st_player(f"{link}")