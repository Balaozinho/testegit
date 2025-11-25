import streamlit as st

# Título do app
st.title("Meu Primeiro App no Streamlit 🎉")

# Entrada de dados
nome = st.text_input("Digite seu nome:")
idade = st.number_input("Digite sua idade:", min_value=0, step=1)

# Botão de ação
if st.button("Gerar Perfil"):
    st.success(f"Olá, {nome}! Você tem {idade} anos.")
    st.balloons()