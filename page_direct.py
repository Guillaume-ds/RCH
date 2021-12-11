import streamlit as st

from streamlit_player import st_player

def page_direct():
    
    st_player("https://www.twitch.tv/reservoirlive")          
    st.markdown("""<iframe src="https://player.twitch.tv/?channel=reservoirlive&parent=mighty-bastion-23461.herokuapp.com"></iframe>""",unsafe_allow_html=True)
