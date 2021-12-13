import streamlit as st 
import streamlit_player as player 
import datetime as dt
import pandas as pd 

def page_historique(nom_direct):
    
    date_deb = st.sidebar.date_input(label="Début",max_value=dt.date.today())
    date_fin = st.sidebar.date_input(label="Fin",max_value=dt.date.today())
    equipe = st.sidebar.selectbox(label="Equipes",value=["Central","L X"])
    
    historique_match = pd.DataFrame({
        "Date":[dt.date.today()],
        "Adversaire":['Central'],
        "Score":["6-12"]
    })
    ajouter_video = st.button(label="Ajouter une vidéo")
    if ajouter_video : 
        historique_match.to_csv()
        
    