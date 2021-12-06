import streamlit as st

from streamlit_player import st_player

def page_direct():
    
    link = st.text_input(label= "Link of the video")
    play = st.button("play the video")
    if play:
        st_player(f"{link}&parent=https://share.streamlit.io/guillaume-ds/rch/main.py")
    
    st.markdown("""<iframe src="https://www.twitch.tv/mauriennisezvous" />
            """, unsafe_allow_html = True)