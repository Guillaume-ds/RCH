import streamlit as st 
import pandas as pd 


st.markdown("""<h1 style='text-align:center; font-weigth:bold; color:rgba(100,100,200,1)'> RCH </h1>""",
            unsafe_allow_html=True)

GPA = st.slider("Ton GPA", min_value=0.00,value=2.0,max_value=4.0,step=0.01)

if GPA <2 : 
    st.write ("Tu es un bernardaud")
    st.image("idiot.jpg",use_column_width=True)
elif GPA >=2 and GPA<2.5 : 
    st.write("Tu es un nulos, tu passes pas")
    st.write("Rejoinds donc la censure")
    st.image("clem.jpg")
elif GPA >=2.5 and GPA<3 : 
    st.write("Pile assez pour passer, suffisament peu pour pas être un IS")
    st.write("Tentes ton premier choix en premier choix")
    st.image("sketch.png")
elif GPA >=3 and GPA<3.9 : 
    st.title("Putain d'IS")
    st.write("T'auras ton premier choix enc*lé, on te juge")
    st.image("groupe.jpg")
elif GPA >=3.9 : 
    st.title("ROTI")
    st.image("orteil.jpg")
    st.image("antoine.png")