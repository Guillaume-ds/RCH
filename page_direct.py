import streamlit as st
import streamlit.components.v1 as components

# embed streamlit docs in a streamlit app


from streamlit_player import st_player

def page_direct():
    
    link = st.text_input(label= "Link of the video")
    link2 = link+"&parent=share.streamlit.io/guillaume-ds/rch/main.py"
    play = st.button("play the video")
    if play:
        st_player(link2)
        st.write(link2)
        st_player(link)
        st.write(link)
        st.video(link)
        components.iframe(link)
        components.iframe(link2)