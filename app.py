import streamlit as st

st.set_page_config(page_title="ChemBase", page_icon="🧪", layout="wide")

# Glosario Técnico Trilingüe
GLOSSARY = {
    "Solución": {"en": "Solution", "it": "Soluzione", "def": "Mezcla homogénea de dos o más sustancias."},
    "Molaridad": {"en": "Molarity", "it": "Molarità", "def": "Moles de soluto por litro de solución (mol/L)."},
    "Normalidad": {"en": "Normality", "it": "Normalità", "def": "Número de equivalentes-gramo de soluto por litro de solución."},
    "Estequiometría": {"en": "Stoichiometry", "it": "Stechiometria", "def": "Relaciones cuantitativas entre reactivos y productos en una reacción."},
    "Titulación": {"en": "Titration", "it": "Titolazione", "def": "Procedimiento cuantitativo para determinar la concentración de un analito."},
    "Grupo Funcional": {"en": "Functional Group", "it": "Gruppo Funzionale", "def": "Átomo o conjunto de átomos responsable de las propiedades químicas de una molécula."}
}

st.sidebar.title("🧪 ChemBase App")
lang = st.sidebar.selectbox("🌐 Idioma / Language / Lingua:", ["Español", "English", "Italiano"])

st.sidebar.markdown("---")
st.sidebar.subheader("📖 Glosario Trilingüe")
term = st.sidebar.selectbox("Selecciona un término:", list(GLOSSARY.keys()))
if term:
    st.sidebar.info(f"**ES:** {term}\n\n**EN:** {GLOSSARY[term]['en']}\n\n**IT:** {GLOSSARY[term]['it']}\n\n*Definición:* {GLOSSARY[term]['def']}")

menu = st.sidebar.radio("Secciones de Estudio:", [
    "🎮 1. Juego de Fundamentos",
    "⚖️ 2. Preparación de Soluciones",
    "📐 3. Matemáticas & Despejes",
    "🧪 4. Química Orgánica e Instrumental",
    "📤 5. Subir Tarea / Corregir Ejercicio en Papel"
])

if menu == "🎮 1. Juego de Fundamentos":
    st.title("🎮 Juego interactivo de Fundamentos Químicos")
    st.write("Aprende y consolida las bases de la química mediante juegos de preguntas y respuestas.")
    
    if "score" not in st.session_state:
        st.session_state.score = 0
        
    st.subheader("Pregunta de Práctica:")
    st.write("¿Cuál es la masa molar aproximada del Hidróxido de Sodio (NaOH)? (Na = 23, O = 16, H = 1)")
    opcion = st.radio("Elige la respuesta correcta:", ["30.0 g/mol", "40.0 g/mol", "58.5 g/mol", "18.0 g/mol"])
    
    if st.button("Comprobar Respuesta"):
        if opcion == "40.0 g/mol":
            st.success("🎉 ¡Correcto! 23 + 16 + 1 = 40 g/mol.")
            st.session_state.score += 10
        else:
            st.error("❌ Incorrecto. Revisa la suma de las masas atómicas.")
    
    st.metric("Puntuación Acumulada", f"{st.session_state.score} pts")

elif menu == "⚖️ 2. Preparación de Soluciones":
    st.title("⚖️ Calculadora & Simulador de Soluciones")
    st.write("Calcula la cantidad exacta de reactivo que debes pesar en el laboratorio.")
    
    pm = st.number_input("Peso Molecular del reactivo (g/mol):", min_value=1.0, value=40.0)
    molaridad = st.number_input("Molaridad deseada (M):", min_value=0.001, value=0.1)
    vol_ml = st.number_input("Volumen a preparar (mL):", min_value=1.0, value=250.0)
    
    gramos = (molaridad * (vol_ml / 1000.0)) * pm
    st.success(f"🧪 **Instrucción de Laboratorio:** Pesa exactamente **{gramos:.4f} g** del reactivo, disuélvelo en agua destilada y lleva a volumen en un matraz aforado de **{vol_ml} mL**.")

elif menu == "📐 3. Matemáticas & Despejes":
    st.title("📐 Despeje de Ecuaciones Químicas")
    st.write("Ecuación de Gases Ideales: PV = nRT")
    despejar = st.selectbox("¿Qué variable deseas calcular?", ["Presión (P)", "Volumen (V)", "Moles (n)", "Temperatura (T)"])
    
    if despejar == "Presión (P)":
        st.latex(r"P = \frac{n \cdot R \cdot T}{V}")
    elif despejar == "Volumen (V)":
        st.latex(r"V = \frac{n \cdot R \cdot T}{P}")
    elif despejar == "Moles (n)":
        st.latex(r"n = \frac{P \cdot V}{R \cdot T}")
    elif despejar == "Temperatura (T)":
        st.latex(r"T = \frac{P \cdot V}{n \cdot R}")

elif menu == "🧪 4. Química Orgánica e Instrumental":
    st.title("🧪 Reconocimiento de Grupos Funcionales e Instrumental")
    st.write("Identifica grupos funcionales clave en español, inglés e italiano.")
    
    gf = st.selectbox("Selecciona un Grupo Funcional:", ["Alcohol (-OH)", "Ácido Carboxílico (-COOH)", "Amina (-NH2)", "Cetona (C=O)"])
    if gf == "Alcohol (-OH)":
        st.info("**Nombre EN:** Alcohol | **Nombre IT:** Alcol\n\n**Característica:** Presencia del grupo hidroxilo. Ejemplo: Etanol.")
    elif gf == "Ácido Carboxílico (-COOH)":
        st.info("**Nombre EN:** Carboxylic Acid | **Nombre IT:** Acido Carbossilico\n\n**Característica:** Grupo carboxilo. Ejemplo: Ácido acético.")

elif menu == "📤 5. Subir Tarea / Corregir Ejercicio en Papel":
    st.title("📤 Carga de Ejercicios Resueltos a Mano")
    st.write("Sube la fotografía de tu ejercicio resuelto en papel para analizar el procedimiento y detectar errores.")
    
    archivo = st.file_uploader("Sube una imagen o PDF:", type=["png", "jpg", "jpeg", "pdf"])
    if archivo is not None:
        st.image(archivo, caption="Ejercicio recibido correctamente para revisión.", use_column_width=True)
        st.success("¡Imagen cargada! En nuestra sesión de revisión evaluaremos el paso a paso.")
