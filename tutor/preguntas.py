import streamlit as st
import numpy as np

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

