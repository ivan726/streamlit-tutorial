# importar librerías
import streamlit as st
import random

# funciones
def iniciar_juego():
    st.session_state["num_secreto"] = random.randint(1, 1000)
    st.session_state["num_intentos"] = 1

# creando la aplicación
if "num_secreto" not in st.session_state:
    iniciar_juego()

st.title(":crystal_ball: Adivinador de número.")
st.write("¡Bienvenido al programa de adivinación! El objetivo es que pueda adivinar un número aleatorio generado entre 1 y 1000.")
st.write("¡Comencemos!")

col1, col2 = st.columns([2, 1])

with col1:
    rta = st.chat_input("Su intento:")
with col2:
    if st.button("Nuevo Juego"):
        iniciar_juego()

if rta:
    st.session_state.num_intentos += 1
    st.chat_message("User").write(rta)

    if int(rta) == st.session_state["num_secreto"]:
        with st.chat_message("ai"):
            st.write("¡Adivinaste! :tada:")
            st.write(f"Número de intentos: {st.session_state.num_intentos}")
            st.balloons()
    else:
        with st.chat_message("ai"):
            if int(rta) > st.session_state["num_secreto"]:
                st.write("El número es más pequeño. :point_down:")
            else:
                st.write("El número es más grande. :point_up_2:")