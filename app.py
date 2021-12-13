import streamlit as st 
import pandas as pd 
import datetime as dt 
import os
from PIL import Image
from dateutil.relativedelta import relativedelta

from page_direct import page_direct
from page_stats import page_stats
from page_historique import page_historique
from data import infos_directs,hr


st.set_page_config(page_title="RCH",layout='wide',page_icon=":rugby_football:")

def main():
    #---------------------------------------------------------PAGES-------------------------------------------------------------------------------
    pages = {
        "Comptage des points en direct": page_direct,
        "Historique des matchs": page_historique,
        "Les stats du RCH": page_stats,
    }

    #--------------------------------------------------------SIDE BAR----------------------------------------------------------------------------- 
    path = os.path.dirname(__file__)
    my_file = path+'/Static/logo_petit.png'
     
    st.sidebar.image(Image.open(my_file))
    st.sidebar.markdown(hr,unsafe_allow_html=True)

    st.sidebar.markdown(f"""<h3 style='text-align: center; font-weight:bold; margin-bottom:-50px;color:rgba(20,10,80,1)'>
                    Choix de la page</h3>""", unsafe_allow_html=True)
    page = st.sidebar.radio("", tuple(pages.keys()))
    st.sidebar.markdown(hr,unsafe_allow_html=True)

    st.sidebar.markdown(f"""<h3 style='text-align: center; font-weight:bold; margin-bottom:-50px;color:rgba(20,10,80,1)'>
                    Choix du direct</h3>""", unsafe_allow_html=True)
    nom_direct = st.sidebar.selectbox('',infos_directs['nom direct'])
    
    #---------------------------------------------------------------Page------------------------------------------------------------------------
    st.markdown("""<h1 style='text-align: center; font-weight:bold;margin-bottom:10px;color:rgba(20,10,80,1); text-decoration: underline rgba(20,10,80,1) 3px;'>
                    Rugby Club HEC</h1>""", unsafe_allow_html=True)
        
    
    pages[page](nom_direct)


#!!!!!!!!!!!!!!!!!!!!!!!!!!!
if __name__ == "__main__":
    main()
#ne pas toucher, cela permet de conserver l'affichage même lorsqu'aucune page n'est sélectionnée





