import streamlit as st 
import pandas as pd 
import datetime as dt 
import os
from PIL import Image
from dateutil.relativedelta import relativedelta

from page_direct import page_direct
from page_stats import page_stats

hr = "<hr style=' text-align : center; border-color : grey; margin-top: 10px; margin-bottom: 15px;'>"
st.set_page_config(page_title="RCH",layout='wide')

def main():
    #---------------------------------------------------------PAGES-------------------------------------------------------------------------------
    pages = {
        "Comptage des points en direct2": page_direct,
        "Les stats du RCH": page_stats,
    }

    #--------------------------------------------------------SIDE BAR----------------------------------------------------------------------------- 
    path = os.path.dirname(__file__)
    my_file = path+'/logo.png'
    st.sidebar.image(Image.open(my_file))
    st.sidebar.markdown(hr,unsafe_allow_html=True)

    page = st.sidebar.radio("Choix de la page", tuple(pages.keys()))
    
    #---------------------------------------------------------------Page------------------------------------------------------------------------
    st.markdown("""<h1 style='text-align: center; font-weight:bold;padding-bottom:15px; margin-bottom:10px;color:rgba(20,10,80,1); text-decoration: underline rgba(20,10,80,1) 3px;'>
                    Rugby Club HEC</h1>""", unsafe_allow_html=True)
        
    
    pages[page]()


#!!!!!!!!!!!!!!!!!!!!!!!!!!!
if __name__ == "__main__":
    main()
#ne pas toucher, cela permet de conserver l'affichage même lorsqu'aucune page n'est sélectionnée





