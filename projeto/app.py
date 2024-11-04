import streamlit as st
import pandas as pd

st.set_page_config(page_title="Loja",
                   page_icon=":bar_chart:",
                   layout="wide"
                  )

# Carregar dados e tratar colunas
df = pd.read_excel(
    io='DadosLoja.xlsx',
    engine='openpyxl',
    sheet_name='Planilha1'
)

# Verificar colunas carregadas
print(df.columns)

# Tratar nomes das colunas
df.columns = df.columns.str.strip().str.capitalize()

# Tratar valores nulos na coluna "Tecido"
df["Tecido"] = df["Tecido"].fillna("Desconhecido")

# Configurar filtros na barra lateral
st.sidebar.header("Filtro")
tecido = st.sidebar.multiselect(
    "Selecione o Tecido:",
    options=df["Tecido"].unique(),
    default=df["Tecido"].unique()
)
cor = st.sidebar.multiselect(
    "Selecione a Cor:",
    options=df["Cor"].unique(),
    default=df["Cor"].unique()
)
df_selection = df.query(
    "Tecido in @tecido and Cor in @cor"
)

# Exibir o DataFrame filtrado
st.dataframe(df_selection)