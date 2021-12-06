import streamlit as st

from streamlit_player import st_player

def page_direct():
    
    link = st.text_input(label= "Link of the video")
    link2 = link+"&parent=share.streamlit.io&parent=share.streamlit.io/guillaume-ds/rch/main.py&parent=localhost:8501"
    play = st.button("play the video")
    if play:
        st_player(link2)
        st.write(link2)
        st_player(link)
        st.write(link)
        
    st.markdown(f"""<iframe 
                src={link}
                allowfullscreen="<allow full screen>">
                </iframe>""", unsafe_allow_html = True)
    st.markdown(f"""<iframe 
                src={link2}
                allowfullscreen="<allow full screen>">
                </iframe>""", unsafe_allow_html = True)