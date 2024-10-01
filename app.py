import streamlit as st
from textblob import TextBlob
from googletrans import Translator

# Inicializar el traductor
translator = Translator()

# Título de la aplicación
st.title('🌟 Análisis de Texto con TextBlob 🌟')

# Subtítulo e instrucciones
st.subheader("Escribe la frase que deseas analizar en el campo de texto a continuación:")

# Información sobre polaridad y subjetividad en la barra lateral
with st.sidebar:
    st.subheader("📊 Polaridad y Subjetividad")
    st.write("""
        **Polaridad:** Indica si el sentimiento expresado en el texto es positivo, negativo o neutral. 
        Su valor oscila entre -1 (muy negativo) y 1 (muy positivo), con 0 representando un sentimiento neutral.
        
        **Subjetividad:** Mide cuánto del contenido es subjetivo (opiniones, emociones, creencias) frente a objetivo (hechos). 
        Va de 0 a 1, donde 0 es completamente objetivo y 1 es completamente subjetivo.
    """)

# Sección para analizar polaridad y subjetividad
with st.expander('🔍 Analizar Polaridad y Subjetividad en un Texto'):
    text1 = st.text_area('Introduce el texto a analizar:')
    if text1:
        blob = TextBlob(text1)
        # Resultados de polaridad y subjetividad
        st.write('**Polaridad:** ', round(blob.sentiment.polarity, 2))
        st.write('**Subjetividad:** ', round(blob.sentiment.subjectivity, 2))
        
        # Evaluación del sentimiento
        sentiment_score = round(blob.sentiment.polarity, 2)
        if sentiment_score >= 0.5:
            st.write('👉 **Sentimiento Positivo** 😊')
        elif sentiment_score <= -0.5:
            st.write('👉 **Sentimiento Negativo** 😔')
        else:
            st.write('👉 **Sentimiento Neutral** 😐')

# Sección para corrección de textos en inglés
with st.expander('📝 Corrección de Texto en Inglés'):
    text2 = st.text_area('Introduce el texto en inglés a corregir:', key='4')
    if text2:
        blob2 = TextBlob(text2)
        corrected_text = blob2.correct()
        st.write('**Texto corregido:**', corrected_text)
