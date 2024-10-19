# MEU PRIMEIRO WEB APP
import streamlit as st
from ACTlib01 import *
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQFwxxM13bxUC0dpyd0w0PxfZIrJ-hp4Px-R6rsTiG3c3n-89JApzA0jYJpU9vNfxeNCvtJ0Cg35KtO/pub?gid=556192647&single=true&output=csv"
db = Ler_GooglePlanilha(url)
db.fillna('', inplace=True)
Escrever(db)

# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("jjk 👍!!")

# Use st.header("") para adicionar um CABEÇALHO ao seu Web app
st.header("sukuna é o melhor 🩸👹")

# Use st.subheader("") para adicionar um SUB CABEÇALHO ao seu Web app
st.subheader("o ser humano é prisioneiro de sua própria liberdade. ele não tem escolha a não ser escolher 🩸")

# Use st.write("") para adicionar um texto ao seu Web app
st.write("como cocê já deve estar ligado st.write() é usado para escrita de texto e informações gerais!")

values = st.slider("Select a range of values", 0.0, 100.0, (5.0, 15.0))
st.write("Values:", values)
