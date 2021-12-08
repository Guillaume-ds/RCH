import streamlit as st
import streamlit.components.v1 as components

from streamlit_player import st_player

def page_direct():
    
    link = st.text_input(label= "Link of the video")
    link2 = link+"&parent=share.streamlit.io/guillaume-ds/rch/main.py"
    play = st.button("play the video")
    if play:
        st_player(link)
        st.write(link)
                
    #st.markdown("""<iframe src="https://player.twitch.tv/?channel=pronewstv" height=" 600" width="900" allowfullscreen="true"></iframe>""",unsafe_allow_html=True)
    st.markdown("""<iframe width="100%" height="100%" src="https://player.twitch.tv/?autoplay=false&channel=channel%3Dpronewstv&parent=share.streamlit.io" allow="accelerometer; autoplay; encrypted-media; picture-in-picture; fullscreen"  style="position: absolute; top: 0px; left: 0px; width: 100%; height: 100%;"></iframe>""",unsafe_allow_html=True)