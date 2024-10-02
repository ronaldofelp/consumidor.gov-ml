import streamlit as st
import pickle
import pandas as pd

def load_data():
    data = pd.read_csv('data/processed/dados_consumidor_gov_to_streamlit.csv')
    return data

def load_model():
    with open('model/modelo_naive_bayes.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

model = load_model()
data = load_data()

st.markdown(
    """
    <style>
    .stApp {
        background-color: #33647a; 
    }

    div[data-baseweb="select"] > div {
        background-color: #f5f5f5; 
        color: #000000; 
        
    }

    .stButton>button {
        background-color: #4CAF50;  

    }
 
    </style>
    """,
    unsafe_allow_html=True
)


st.title('Preditor de avaliação negativa')


st.subheader('Insira os dados do cliente para prever a avaliação da reclamação')


regiao = st.selectbox('Região', list(data['regiao'].unique()))
uf = st.selectbox('UF',list(data['uf'].unique()))
cidade = st.selectbox('Cidade', list(data['cidade'].unique()))
sexo = st.selectbox('Sexo', ['M', 'F', 'O'])
faixa_etaria = st.selectbox('Faixa Etária', list(data['faixa_etaria'].unique()))
data_finalizacao = st.selectbox('Mês de Finalização', list(range(1, 13)))
nome_fantasia = st.selectbox('Nome Empresa',list(data['nome_fantasia'].unique()))
area = st.selectbox('Área',list(data['area'].unique()))
assunto = st.selectbox('Assunto',list(data['assunto'].unique()))
grupo_problema = st.selectbox('Grupo de Problema', list(data['grupo_problema'].unique()))
problema = st.selectbox('Problema',list(data['problema'].unique()))
como_comprou_contratou = st.selectbox('Como comprou/contratou', list(data['como_comprou_contratou'].unique()))
procurou_empresa = st.selectbox('Procurou a empresa antes de reclamar?', ['S', 'N'])
respondida = st.selectbox('A empresa respondeu?', ['S', 'N'])



input_data = [[regiao, uf, cidade, sexo, faixa_etaria, data_finalizacao,
                        nome_fantasia, area, assunto, grupo_problema, problema,
                        como_comprou_contratou, procurou_empresa, respondida]]


columns = ['regiao', 'uf', 'cidade', 'sexo', 'faixa_etaria', 'data_finalizacao',
       'nome_fantasia', 'area', 'assunto', 'grupo_problema', 'problema',
       'como_comprou_contratou', 'procurou_empresa', 'respondida']

input_data = pd.DataFrame(input_data, columns=columns)


if st.button('Fazer Previsão'):
    
  
    prediction = model.predict_proba(input_data)[0][2]
  
    prob_formatada = round(prediction * 100, 2)
    
    st.write(f'A probabilidade desse consumidor avaliar negativamente a reclamação é de: {prob_formatada}%')

