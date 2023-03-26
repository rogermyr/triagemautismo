import streamlit as st
import numpy as np
import pandas as pd
import pickle

st.set_page_config(page_title="Triagem de Autismo Leve em Adultos", page_icon="chart_with_upwards_trend", layout="centered", initial_sidebar_state = "auto")

model = pickle.load(open('model.pkl','rb'))

def predict(A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, genero, ictericia, familiar):
    #Predicting the price of the carat    
    if A1 == 'Concordo Plenamente' or A1 == 'Concordo Parcialmente':
        A1 = 1
    else:
        A1 = 0

    if A7 == 'Concordo Plenamente' or A7 == 'Concordo Parcialmente':
        A7 = 1
    else:
        A7 = 0

    if A8 == 'Concordo Plenamente' or A8 == 'Concordo Parcialmente':
        A8 = 1
    else:
        A8 = 0

    if A10 == 'Concordo Plenamente' or A10 == 'Concordo Parcialmente':
        A10 = 1
    else:
        A10 = 0

    if A2 == 'Concordo Plenamente' or A2 == 'Concordo Parcialmente':
        A2 = 0
    else:
        A2 = 1

    if A3 == 'Concordo Plenamente' or A3 == 'Concordo Parcialmente':
        A3 = 0
    else:
        A3 = 1

    if A4 == 'Concordo Plenamente' or A4 == 'Concordo Parcialmente':
        A4 = 0
    else:
        A4 = 1

    if A5 == 'Concordo Plenamente' or A5 == 'Concordo Parcialmente':
        A5 = 0
    else:
        A5 = 1

    if A6 == 'Concordo Plenamente' or A6 == 'Concordo Parcialmente':
        A6 = 0
    else:
        A6 = 1

    if A9 == 'Concordo Plenamente' or A9 == 'Concordo Parcialmente':
        A9 = 0
    else:
        A9 = 1

    df = pd.DataFrame(np.array([[A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,genero,ictericia,familiar]]),
                      columns=['A1_Score','A2_Score','A3_Score','A4_Score','A5_Score','A6_Score','A7_Score','A8_Score','A9_Score','A10_Score','gender','jundice','autism'])                      
    df2 = pd.get_dummies(df, columns=['gender','jundice','autism'])
    df2 = df2.reindex(columns=model.feature_names_in_, fill_value=0)
    prediction = model.predict(df2)
    if prediction == 0:
        return 'NEGATIVO. Não há suspeitas para o autismo.'
    else:
        return 'POSITIVO. Há suspeitas para o autismo. É aconselhado procurar um Psiquiatra ou Neurologista especializado no Transtorno do Espectro Autista.'

st.markdown("<h4 style='text-align: center; color: yellow; font-weight: bold'>Ferramenta de Triagem de Autismo Leve em Adultos</h4>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;font-weight: bold; color: white'>Desenvolvido por: Rogério Henriques Silva.", unsafe_allow_html=True)    
st.markdown("<p style='text-align: center;font-weight: bold; color: white'>Curso: MBA em Data Science & Analytics - USP/ESALQ</p>", unsafe_allow_html=True)    
col1, col2, col3 = st.columns(3)

with col1:
    pass

with col2:
    st.image("autismo.png", width=150)

with col3:
    pass

st.sidebar.write("Preencha as seguintes informações abaixo")
genero = st.sidebar.radio("Gênero:", ('Masculino', 'Feminino'),horizontal=True) 
ictericia = st.sidebar.radio("Nasceu com icterícia?", ('Sim', 'Não'),horizontal=True) 
familiar = st.sidebar.radio("Possui algum familiar de 1º Grau diagnosticado com autismo? ", ('Sim', 'Não'),horizontal=True)
A1 = st.sidebar.radio("Costumo notar pequenos sons quando outros não percebem: ", ('Concordo Plenamente', 'Concordo Parcialmente', 'Discordo Parcialmente', "Discordo Plenamente"))
A2 = st.sidebar.radio("Eu geralmente me concentro mais no todo de uma imagem, ao invés de pequenos detalhes: ", ('Concordo Plenamente', 'Concordo Parcialmente', 'Discordo Parcialmente', "Discordo Plenamente"))
A3 = st.sidebar.radio("Acho fácil fazer mais de uma coisa de uma só vez: ", ('Concordo Plenamente', 'Concordo Parcialmente', 'Discordo Parcialmente', "Discordo Plenamente"))
A4 = st.sidebar.radio("Se houver uma interrupção, posso voltar para o que eu estava fazendo muito rápido: ", ('Concordo Plenamente', 'Concordo Parcialmente', 'Discordo Parcialmente', "Discordo Plenamente"))
A5 = st.sidebar.radio("Acho fácil “ler nas entrelinhas” quando alguém está falando comigo: ", ('Concordo Plenamente', 'Concordo Parcialmente', 'Discordo Parcialmente', "Discordo Plenamente"))
A6 = st.sidebar.radio("Eu sei dizer se alguém que está me ouvindo está ficando entediado: ", ('Concordo Plenamente', 'Concordo Parcialmente', 'Discordo Parcialmente', "Discordo Plenamente"))
A7 = st.sidebar.radio("Quando estou lendo uma história, acho difícil descobrir as intenções dos personagens: ", ('Concordo Plenamente', 'Concordo Parcialmente', 'Discordo Parcialmente', "Discordo Plenamente"))
A8 = st.sidebar.radio("Gosto de coletar informações sobre categorias de coisas (por exemplo, tipos de carro, tipos de pássaros, tipos de trem, tipos de planta, etc.): ", ('Concordo Plenamente', 'Concordo Parcialmente', 'Discordo Parcialmente', "Discordo Plenamente"))
A9 = st.sidebar.radio("Acho que é fácil descobrir o que alguém está pensando ou sentindo apenas olhando para o rosto da pessoa: ", ('Concordo Plenamente', 'Concordo Parcialmente', 'Discordo Parcialmente', "Discordo Plenamente"))
A10 = st.sidebar.radio("Acho difícil entender as intenções das pessoas: ", ('Concordo Plenamente', 'Concordo Parcialmente', 'Discordo Parcialmente', "Discordo Plenamente"))

hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: rgb(0, 38, 255);
}
</style>""", unsafe_allow_html=True)


if not st.sidebar.button('RESULTADO'):
    st.markdown("<p style='text-align: center'>Esta ferramenta tem por objetivo realizar uma análise preditiva em adultos que possuem suspeitas de serem autistas. Caso o resultado seja “POSITIVO” para o Autismo, será recomendado que se busque um Psiquiatra ou Neurologista especialistas em TEA para que seja feito um diagnóstico clínico e, caso confirmado, que seja iniciado o tratamento.</p>", unsafe_allow_html=True)        
else:
    result = predict(A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, genero, ictericia, familiar)
    st.success(result)
