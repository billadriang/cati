import streamlit as st
import time

# Título de la aplicación
st.title("Te invito a una cita cielito ❤️")

# Estado inicial
if 'clicked' not in st.session_state:
    st.session_state.clicked = False

# Función para manejar el clic
def on_click():
    st.session_state.clicked = True

# Mostrar la carta si no ha sido clickeada
if not st.session_state.clicked:
    if st.button("📧", on_click=on_click):
        st.session_state.clicked = True

# Mostrar la animación y la invitación si la carta ha sido clickeada
else:
    with st.spinner('Abriendo la carta...'):
        time.sleep(2)  # Simula una animación con un delay de 2 segundos
    st.image("invitacion.png", caption="Manana sabado a 27 de Julio a las 20:30 por Metro Manuel Montt", use_column_width=True)
    st.markdown("[Click aca cielo📍](https://www.tiktok.com/@pintart.chile/video/7348144975013481734)")