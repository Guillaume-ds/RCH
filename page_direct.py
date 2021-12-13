import streamlit as st
from streamlit_player import st_player
from streamlit_autorefresh import st_autorefresh
import time
from data import infos_directs
import pandas as pd
import datetime as dt 


def page_direct(nom_direct):
    
    #---------------------------------------------------------Fonctions--------------------------------------------------------------
    @st.cache
    def donnees_direct(nom_direct):
        """
        Récupère les principales informations sur le live
        """        
        infos_direct = infos_directs.loc[infos_directs['nom direct']==nom_direct]
        equipe_rch = infos_direct['equipe RCH'].item()
        equipe_adverse = infos_direct['equipe adverse'].item()
        chaine = infos_direct['chaine'].item()
        commentaires_file = infos_direct['commentaires'].item()
        return equipe_rch,equipe_rch,equipe_adverse,chaine,commentaires_file

    equipe_rch,equipe_rch,equipe_adverse,chaine,commentaires_file = donnees_direct(nom_direct)
        
    @st.cache
    def display_direct(chaine): 
        """
        Prépare l'embedding
        """           
        video = f"""<iframe src="https://player.twitch.tv/?channel={chaine}&parent=rchendirect.herokuapp.com&parent=localhost"
                        width=100%
                        height="500"
                        allowfullscreen="<allowfullscreen>"></iframe>"""     
        chat = f"""<iframe id="twitch-chat-embed"
                        src="https://www.twitch.tv/embed/{chaine}/chat?parent=localhost"
                        height="500"
                        width=100%>
                        </iframe>"""            
        return video,chat
    
    def recuperation_commentaires(commentaires_file):
        """
        Récupère les commentaires liés au live scoring
        """
        commentaires = pd.read_csv('Static/'+commentaires_file)
        i = max(commentaires.index)
        score_rch = commentaires.loc[i,'score RCH']
        score_adversaire = commentaires.loc[i,'score adverse']
        return commentaires,score_rch,score_adversaire
    
    commentaires,score_rch,score_adverse = recuperation_commentaires(commentaires_file)
    
    def save_nouveau_direct(equipe_rch,equipe_adverse,nouvelle_chaine):
        """
        Initie un nouveau live scoring
        """
        infos_directs = pd.read_csv("Static/infos_directs.csv") 
        infos_directs = infos_directs.append({
                        "equipe RCH":equipe_rch,
                        "equipe adverse":equipe_adverse,
                        "chaine":nouvelle_chaine,
                        "nom direct":equipe_rch+equipe_adverse.str(dt.date.today()),
                        "commentaires":"commentaires"+equipe_rch+equipe_adverse+str(dt.date.today()+".csv"),
                        "replay":[]},
                        ignore_index=True)
        infos_directs.to_csv("Static/infos_directs.csv")
        commentaires = pd.DataFrame({
            "equipe RCH":equipe_rch,
            "equipe adverse":equipe_adverse,
            "score RCH":0,
            "score adverse":0,
            "minute":0,
            "commentaire":"demoiselles baissez les fifres",
            "nom":"RCH en direct"
        })  
        commentaires.to_csv("commentaires"+equipe_rch+equipe_adverse+str(dt.date.today())+".csv",ignore_index=True)
    
    def nouveau_commentaire(score_rch,score_adverse,minute,commentaire,nom):
        """
        Ajoute un commentaire avec le score
        """
        commentaires = pd.read_csv('Static/'+commentaires_file)
        commentaires = commentaires.append({"equipe RCH":equipe_rch,
                                            "equipe adverse":equipe_adverse,
                                            "score RCH":score_rch,
                                            "score adverse":score_adverse,
                                            "minute":minute,
                                            "commentaire":commentaire,
                                            "nom":nom},
                                            ignore_index=True)
        commentaires.to_csv("Static/"+commentaires_file,
                            index=False) 
        st.write(commentaires) 
    
    #---------------------------------------------------------Sidebar direct--------------------------------------------------------------
    
    st.sidebar.markdown("<hr style=' text-align : center; border-color : grey; margin-top: 10px; margin-bottom: 10px;'>",unsafe_allow_html=True)    
    
    st.sidebar.markdown(f"""<h3 style='text-align: center; font-weight:bold; margin-bottom:0px;color:rgba(20,10,80,1)'>
                    Nouveau direct</h3>""", unsafe_allow_html=True)
    
    nouvelle_equipe_rch = st.sidebar.text_input("Equipe RCH",placeholder="RCH 1")
    nouvelle_equipe_adverse = st.sidebar.text_input(label="Equipe adverse",placeholder="Les demoiselles")
    nouvelle_chaine = st.sidebar.text_input(label="Chaine du direct")    
    lancement_direct = st.sidebar.button(label="Démarrer le direct")
    
    if lancement_direct:
        try :
            save_nouveau_direct(nouvelle_equipe_rch,nouvelle_equipe_adverse,nouvelle_chaine)
            st.success('Comptage en direct ajouté')
        except:
            st.error('Impossible d\'ajouter le comptage')
            
    #---------------------------------------------------------------Video-------------------------------------------------------------------
    
    titre = st.markdown(f"""<h3 style='text-align: center; font-weight:bold; margin-bottom:0px;color:rgba(20,10,80,1)'>
                    {equipe_rch} : {score_rch} - {score_adverse} : {equipe_adverse}</h3>""", unsafe_allow_html=True)
            
    col1,col2 = st.columns([3,1])      
    video,chat = display_direct(chaine)
    col1.markdown(video,unsafe_allow_html = True)
    col2.markdown(chat,unsafe_allow_html = True)
    st.markdown("<hr style=' text-align : center; border-color : white; margin-top:40px;margin-bottom:10px;'>",unsafe_allow_html=True)
    #----------------------------------------------------------Ajout points------------------------------------------------------------------
    with st.expander('Modifier le score:'):
        st.markdown(f"""<h4 style='text-align: center; font-weight:bold; margin-top:-10px;margin-bottom:0px;color:rgba(20,10,80,1)'>
                        Modifier le score:</h4>""", unsafe_allow_html=True)
        st.markdown("<hr style=' text-align : center; border-color : grey; margin-top:0px;margin-bottom:10px;'>",unsafe_allow_html=True) 
        
        col1,col2,col3 = st.columns(3)
        nouveau_score_rch = col1.number_input(label=equipe_rch,value=score_rch)
        nouveau_score_adverse = col2.number_input(label=equipe_adverse,value=score_adverse)
        minute_nouveau_score = col3.number_input(label='Minute',value = 0)
        
        col1,col2,col3 = st.columns([4,1,4])
        ajout_score = col2.button('Ajouter le score')
        
        if ajout_score:        
            try:
                nouveau_commentaire(nouveau_score_rch,nouveau_score_adverse,minute_nouveau_score,"Nouvel essai!","RCH en direct")
                st.success('Nouveau score ajouté')
            except:
                st.error('Impossible d\'ajouter le score')
        
        
    
    #----------------------------------------------------------Ajout points------------------------------------------------------------------
    with st.expander('Ajouter un commentaire:'):
        st.markdown(f"""<h4 style='text-align: center; font-weight:bold; margin-top:-10px;margin-bottom:10px;color:rgba(20,10,80,1)'>
                        Ajouter un commentaire (hors du chat):</h4>""", unsafe_allow_html=True)
        
        col1,col2,col3 = st.columns([4,1,1])
        text_nouveau_commentaire = col1.text_area(label="Commentaire")    
        nom_commentateur = col2.text_input(label="Nom commentateur")
        minute_nouveau_commentaire = col2.number_input(label='Minute',value = 0,key='Commentaire')
        col3.write(' ')
        col3.write(' ')
        ajout_commentaire = col3.button('Ajouter le commentaire')
        
        if ajout_commentaire:        
            try:
                nouveau_commentaire(score_rch,score_adverse,minute_nouveau_commentaire,text_nouveau_commentaire,nom_commentateur)
                st.success('Nouveau commentaire ajouté')
            except:
                st.error('Impossible d\'ajouter le commentaire')

    st.markdown("<hr style=' text-align : center; border-color : white; margin-top:50px;margin-bottom:10px;'>",unsafe_allow_html=True)
    col1,col2,col3= st.columns([4,1,1])
    for i in range(len(commentaires)):
        col1.write(commentaires.loc[i,'commentaire'])
        col2.write(commentaires.loc[i,'nom'])
        col3.write(commentaires.loc[i,'minute'])
        st.markdown("<hr style=' text-align : center; border-color : white; margin-top:20px;margin-bottom:10px;'>",unsafe_allow_html=True)
        
    st_autorefresh(interval=10 * 1000)
    

        
    

    
     
    
     