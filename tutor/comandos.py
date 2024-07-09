import streamlit as st

st.title(":blue[Resumen:] Comandos en streamlit")

# elementos de texto
st.subheader("Elementos de texto", divider="blue")

with st.expander("Títulos"):
    with st.echo():
        st.title("Príncipal")
        st.header("Título")
        st.subheader("Subtítulo")

with st.expander("Markdown"):
    with st.echo():
        st.markdown('''
        Markdown es un lenguaje de marcado ligero que te permite escribir texto plano con formato, de manera sencilla y legible.

        Se pueden escribir:
        - Texto en **negrilla**
        - Texto en *cursiva*
        - Texto ***combinado***

        ---

        También se pueden escribir:
        1. Ecuaciones en una línea como $x=5$.
        2. Ecuaciones centradas como 
        $$
        x = 10.
        $$
        ''')

with st.expander("Ecuaciones en latex"):
    with st.echo():
        st.latex("\\frac{df}{dx} = \\lim_{h \\rightarrow 0} \\frac{f(x+h) - f(x)}{h}")

with st.expander("Divisores de texto"):
    with st.echo():
        st.divider()


# Elementos multimedia
st.subheader("Elementos multimedia", divider="blue")

with st.expander("Imagenes"):
    with st.echo():
        st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.svg")

with st.expander("Videos"):
    with st.echo():
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")


# Elementos de entrada de datos
st.subheader("Elementos de entrada de datos", divider="blue")

with st.expander("Entrada de texto"):
    with st.echo():
        nom = st.text_input("nombre:")
        st.write(f"Hola, {nom}!")
    
    st.divider()

    with st.echo():
        msj = st.text_area("Contador", value="Hola mundo,", height=10)
        npals = len(msj.split(" "))
        st.write(f"El mensaje ingresado tiene {npals} palabras.")


with st.expander("Entrada de dato numéricos"):
    with st.echo():
        edad = int(st.number_input("Edad", min_value=0, max_value=100))
        if edad >= 18:
            st.write("Eres mayor de edad.")
        else:
            st.write("Eres menor de edad.")
    
    st.divider()

    with st.echo():
        num = int(st.slider("tabla:", min_value=1, max_value=12))
        for i in range(1,13,1):
            st.write(f"{num} x {i} = {num*i}")

with st.expander("Selección de una opción"):
    with st.echo():
        opc = st.selectbox("Figura:", ["Triangulo", "Circulo", "Cuadrado"])
        if opc == "Triangulo":
            st.latex("A = \\frac{b h}{2}")
        elif opc == "Circulo":
            st.latex("A = \\pi r^2")
        elif opc == "Cuadrado":
            st.latex("A = b^2")

with st.expander("Generar acción mediante botones"):
    with st.echo():
        clic = st.button("Presionar")
        if clic:
            st.write("Has presionado el botón.")

# layouts
st.subheader("Layouts", divider="blue")

with st.expander("Columnas"):
    with st.echo():
        col1, col2 = st.columns(2)
        with col1:
            st.write("Texto en la primera columna.")
        with col2:
            st.write("Texto en la segunda columna.")
    
    st.divider()

    with st.echo():
        col1, col2, col3 = st.columns([1,2,1])
        with col1:
            st.write("Esta columna tiene el 25\\% del ancho.")
        with col2:
            st.write("Esta columna tiene la mitad del ancho.")
        with col3:
            st.write("Esta columna tiene el 25\\% del ancho.")

with st.expander("Contenedores"):
    with st.echo():
        with st.container(border=True):
            st.write("Texto en el contenedor.")