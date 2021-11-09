import streamlit as st 
import pandas as pd 


st.markdown("""<h1 style='text-align:center; font-weigth:bold; color:rgba(100,100,200,1)'> RCH </h1>""",
            unsafe_allow_html=True)

GPA = st.slider("Ton GPA", min_value=0.00,value=2.0,max_value=4.0,step=0.01)

if GPA >=0 and GPA <0.5 : 
    st.title ("AlainNNN Seize ")
    st.image("saiz.png",use_column_width=True)
    st.caption("coucou")
elif GPA >=0.5 and GPA<2: 
    st.title ("Va plutôt à la messe")
    st.image("bambo.PNG",use_column_width=True)
elif GPA >=2 and GPA<2.5 : 
    st.write("Tu es un nulos, tu passes pas")
    st.write("Rejoinds donc la censure")
    st.image("clem.jpg")
elif GPA >=2.5 and GPA<3 : 
    st.write("Pile assez pour passer, suffisament peu pour pas être un IS")
    st.write("Tentes ton premier choix en premier choix")
    st.image("sketch.png")
elif GPA >=3 and GPA<3.5 :
    st.write("Ppresque indigne du RCH...")
    st.write("On va te racadrer")
    st.image("nkla.jpg")
elif GPA >=3.5 and GPA<3.9 : 
    st.title("Putain d'IS")
    st.write("T'auras ton premier choix enc*lé, on te juge")
    st.image("groupe.jpg")
elif GPA >=3.9 : 
    st.title("ROTI")
    st.image("orteil.jpg")
    st.image("antoine.png")
    
st.sidebar.markdown("""
<hr> 
""", unsafe_allow_html=True)
st.title('Calcul ton IMCroutard')
col1,col2 = st.columns(2)
Taille_Meuf = col1.number_input("Taille de la meuf (en cm)",value=1)
Poids_Meuf = col2.number_input("Poids de la meuf",value=1)
Taille_Mec = col1.number_input("Taille du mec (en cm)",value=1)
Poids_Mec = col2.number_input("Poids du mec",value=1)

st.markdown(f""" <p style='text-align:center; font-weigth:bold;'>Ton croutaromètre : <em>{(Taille_Meuf/(Poids_Meuf**2))/(Taille_Mec/(Poids_Mec**2))}</em> </p> """, unsafe_allow_html = True)




