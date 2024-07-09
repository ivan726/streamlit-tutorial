import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("seaborn-v0_8-whitegrid")

st.title(":question: Algunas :red[preguntas]")

with st.expander("¿Cómo se podría ingresar una matriz en Streamlit?"):
    st.markdown("Con un elemento `st.data_editor()` que permite generar una tabla dinámica. En el siguiente ejemplo la matriz queda almacenada en la variable `mat` como un numpy array.")

    with st.echo():
        c1, c2 = st.columns([1,3], gap="large")

        with c1:
            nfil = int(st.number_input("Filas:", value=2, min_value=1))
            ncol = int(st.number_input("Columnas:", value=2, min_value=1))
        
        with c2:
            mat = st.data_editor(np.zeros((nfil, ncol)), use_container_width=True, column_config={str(c):st.column_config.NumberColumn('') for c in range(ncol)})


with st.expander("¿Cómo se podría ingresar un rango en Streamlit?"):
    st.markdown("La mejor forma para ingresar un rango en streamlit es utilizando un `st.slider()`. En este caso se utiliza un parámtero de `value` asignando una tupla con los valores inicial y final del rango. En este ejemplo los valores de inicio y final quedan guardados en `ini` y `fin`, respectivamente.")
    with st.echo():
        ini, fin = st.slider("Rango:", 0, 100, value=(10, 30))
        ini = int(ini)
        fin = int(fin)
        st.write(f"Rango ingresado: $[{ini}, {fin}]$")

with st.expander("¿Cómo puedo graficar valores tabulados?"):
    with st.echo():
        c1, c2 = st.columns([1, 3])
        with c1:
            num = int(st.number_input("Número de datos a ingresar:", value=3))
            datos = np.zeros((num, 2))
            datos[:, 0] = np.arange(num)
            datos[:, 1] = np.random.randint(-10, 10, num)
            datos = st.data_editor(datos, use_container_width=True, column_config={"0":st.column_config.NumberColumn("x"), "1":st.column_config.NumberColumn("y")})

        with c2:
            fig, ax = plt.subplots()
            ax.plot(datos[:,0], datos[:,1])
            ax.axvline(0, color="gray")
            ax.axhline(0, color="gray")
            st.pyplot(fig)

with st.expander("¿Cómo puedo tabular una función?"):
    with st.echo():
        c1, c2 = st.columns([1,3])
        with c1:
            st.markdown("""
            **Función a graficar:** 
            $$
            f(x) = x^2
            $$""")
            num = int(st.number_input("Puntos:", value=3))

            c11, c12 = st.columns(2)
            with c11:
                datos_x = np.linspace(-5, 5, num)
                datos_x = st.data_editor(datos_x, use_container_width=True, column_config={"value":st.column_config.NumberColumn("x")})
            with c12:
                datos_y = datos_x**2
                datos_y = st.data_editor(datos_y, use_container_width=True, column_config={"value":st.column_config.NumberColumn("f(x)", disabled=True)})

        with c2:
            # creando vectores de la curva
            vec_x = np.linspace(min(datos_x), max(datos_x), 100)
            vec_y = vec_x**2

            fig, ax = plt.subplots()        # grafico
            ax.axvline(0, color="gray")     # eje x
            ax.axhline(0, color="gray")     # eje y
            ax.plot(vec_x, vec_y)           # linea
            ax.scatter(datos_x, datos_y, zorder=2)      # puntos
            st.pyplot(fig)                  # mostrar


