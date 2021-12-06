import streamlit as st

from streamlit_player import st_player

def page_direct():
    
    lien = st.text_input(label= "Lien du direct")
    lancement = st.button("Lancer le direct")
    if lancement:
        st_player(f"{lien}")