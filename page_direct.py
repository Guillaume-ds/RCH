import streamlit as st
import streamlit.components.v1 as components

from streamlit_player import st_player

def page_direct():
    
    st_player("https://www.twitch.tv/reservoirlive")          
    st.markdown("""<iframe src="https://player.twitch.tv/?channel=reservoirlive&parent=share.streamlit.io"></iframe>""",unsafe_allow_html=True)
