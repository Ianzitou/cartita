import streamlit as st
from PIL import Image
import time

# Configuración de la página
st.set_page_config(page_title="Un mensaje especial", page_icon="💛", layout="centered")

# Inicializa el estado de la pantalla
if "pantalla" not in st.session_state:
    st.session_state.pantalla = 1

# Funciones para cambiar de pantalla
def mostrar_mas():
    st.session_state.pantalla = 2
    st.rerun()

def volver_inicio():
    st.session_state.pantalla = 1
    st.rerun()

# Diseño de la página con fondo lila
st.markdown(
    """
    <style>
        body {
            background-color: #F5E6F7;
        }
        .message {
            font-size: 22px;
            text-align: center;
            font-weight: bold;
            color: #6A0572;
            padding: 20px;
        }
        .button-container {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Pantalla 1 - Mensaje especial
if st.session_state.pantalla == 1:
    st.markdown("<div class='message'>Hola, jsjsj</div>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class='message'>
        Hoy es el día de dar flores amarillas a las personas que quieres que se queden contigo. Bueno, aquí está mi intento de que te quedes conmigo.
        No creo que sea necesario unas flores para expresarte lo que siento porque trato día a día de demostrarte que no quiero que te vayas de mi vida.<br><br>
        Pero sé la ilusión y lo bonito que se siente, por lo tanto, aunque no te las pueda dar físicamente, esta es mi forma de mostrarte cuánto me importas.<br><br>
        Muack 💛<br><br>
        <b>Att: Tu admirador secreto</b>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("<div class='button-container'>", unsafe_allow_html=True)
    if st.button("Muestrame más 💛"):
        mostrar_mas()
    st.markdown("</div>", unsafe_allow_html=True)

# Pantalla 2 - Imagen del ramo de flores
elif st.session_state.pantalla == 2:
    with st.spinner("Cargando sorpresa..."):
        time.sleep(1.5)

    try:
        image_path = "girasoles.png"  # Asegúrate de que la imagen esté en la misma carpeta
        image = Image.open(image_path)
        st.image(image, caption="mira mira ,pada ti", use_container_width=True)
    except FileNotFoundError:
        st.error("No se encontró la imagen 'girasoles.png'. Asegúrate de que esté en la misma carpeta que el archivo .py")

    st.markdown("<div class='message'>Espero que esto te haya sacado una sonrisa 💛</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='button-container'>", unsafe_allow_html=True)
    if st.button("Ota vez 🔁"):
        volver_inicio()
    st.markdown("</div>", unsafe_allow_html=True)
