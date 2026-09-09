import streamlit as st

st.set_page_config(page_title="ChemBase", page_icon="🧪")

st.title("🧪 ChemBase App")
st.write("¡Bienvenida a tu aplicación de estudio de Química!")

lang = st.selectbox("🌐 Idioma / Language / Lingua:", ["Español", "English", "Italiano"])

st.info("App configurada correctamente. ¡Lista para cargar tus temas y ejercicios!")
