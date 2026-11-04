import os
from urllib.parse import quote
import streamlit as st

st.set_page_config(page_title="Portafolio de Camilo", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bangers&display=swap');
.stApp {
    background-color: #fff3c4;
    background-image: radial-gradient(#ff7a59 2px, transparent 2px);
    background-size: 24px 24px;
}
[data-testid="stSidebar"] {
    background: #b9a7ff;
    border-right: 6px solid black;
}
h1, h2, h3 {
    font-family: 'Bangers', cursive;
    letter-spacing: 1px;
    color: black;
}
[data-testid="stVerticalBlockBorderWrapper"] {
    background: white;
    border: 4px solid black;
    border-radius: 12px;
    box-shadow: 8px 8px 0px black;
}
img {
    border: 3px solid black;
    border-radius: 10px;
}
.btn {
    display: inline-block;
    background: #ff4f81;
    color: white !important;
    font-family: 'Bangers', cursive;
    font-size: 20px;
    padding: 8px 18px;
    border: 3px solid black;
    border-radius: 10px;
    box-shadow: 4px 4px 0px black;
    text-decoration: none;
}
</style>
""", unsafe_allow_html=True)


def imagen(base, titulo):
    for ext in ("png", "jpg", "jpeg"):
        ruta = f"{base}.{ext}"
        if os.path.exists(ruta):
            return ruta
    return "https://placehold.co/400x300?text=" + quote(titulo)


trabajos = [
    {"titulo": "Welcome to Japan", "imagen": "tokyo",
     "texto": "Un viaje por Japón contado en cuatro capítulos: Tokyo, Kyoto, Osaka y el Monte Fuji.",
     "link": "https://myfirstwb-thekingoff.streamlit.app/"},
    {"titulo": "Fábulas de Japón", "imagen": "japan",
     "texto": "Fábulas japonesas divididas en escenas que puedes escuchar con texto a voz, en varios idiomas.",
     "link": "https://appfirstmod.streamlit.app/"},
    {"titulo": "Traductor de viaje", "imagen": "traductor",
     "texto": "Habla o escribe, y escucha la traducción al instante en varios idiomas.",
     "link": "https://traductor-viaje-cx9t8wclqvqvinzqcacmfm.streamlit.app/"},
    {"titulo": "Análisis de sentimiento", "imagen": "sentimiento",
     "texto": "Escribe un texto y la app analiza su sentimiento y responde con una interacción.",
     "link": "https://sentimentclase8-jnptjgg6393lx8pgdssra3.streamlit.app/"},
    {"titulo": "Detective de textos", "imagen": "detective",
     "texto": "Un detective investiga tu texto: su ánimo, sus palabras clave y sus frases más extremas.",
     "link": "https://gzcfwslbxlyqnwpgguglh9.streamlit.app/"},
    {"titulo": "TF-IDF en español", "imagen": "tfidf",
     "texto": "Una demo de TF-IDF aplicada a textos en español para ver qué palabras pesan más.",
     "link": "https://tdfesp1-7zknjf6fmguneabd4k2xxb.streamlit.app/"},
    {"titulo": "Escáner de letras", "imagen": "escaner",
     "texto": "Sube una foto con texto y el escáner lo convierte en texto editable, con nivel de confianza.",
     "link": "https://clase7-2-vrdw4xw4tf4gjiz3xm2znc.streamlit.app/"},
    {"titulo": "Lector de carteles", "imagen": "lector",
     "texto": "Apunta a un cartel o menú: la app lee el texto, lo traduce y te lo dice en voz alta.",
     "link": "https://iayrgu42wysaekgqeacxiv.streamlit.app/"},
    {"titulo": "Inventario de mi cuarto", "imagen": "inventario",
     "texto": "Toma una foto de tu espacio y la IA detecta los objetos con YOLO y arma el inventario en español.",
     "link": "https://ymj4oatrspyaunw7npduzt.streamlit.app/"},
    {"titulo": "Joystick de mano", "imagen": "joystick",
     "texto": "Tu mano es el joystick: señala una dirección y un modelo de Teachable Machine mueve un robot hasta la estrella.",
     "link": "https://joystick-mano-aj3u4xhpdvrtk5mysmkbmf.streamlit.app/"},
]

st.title("¡Mis trabajos del semestre!")
st.write("Explora las aplicaciones y pruébalas en vivo.")

with st.sidebar:
    st.subheader("Sobre mí")
    st.write("Camilo, estudiante de Diseño Interactivo en la Universidad EAFIT.")
    st.write("Estas son las 10 aplicaciones de inteligencia artificial que hice durante el semestre.")
    st.subheader("Contacto")
    st.markdown('<a class="btn" href="https://github.com/Noctisdc">Mi GitHub</a>', unsafe_allow_html=True)

for i in range(0, len(trabajos), 3):
    columnas = st.columns(3)
    for col, t in zip(columnas, trabajos[i:i + 3]):
        with col:
            with st.container(border=True):
                st.subheader(t["titulo"])
                st.image(imagen(t["imagen"], t["titulo"]))
                st.write(t["texto"])
                st.markdown(f'<a class="btn" href="{t["link"]}">Ver trabajo</a>', unsafe_allow_html=True)
