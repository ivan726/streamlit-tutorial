import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("ggplot")

st.title("Ecuación cuadrática.")

st.markdown('''
Una **ecuación cuadrática** es una ecuación de la forma:
$$
ax^2 + bx + c = 0,
$$
con $a$, $b$ y $c$ siendo coeficientes reales y $a \\neq 0$.
''')

with st.container(border=True):
    st.markdown("##### **Digite los coeficientes de su ecuación:**")
    col1, col2, col3 = st.columns(3, gap="medium")

    with col1:
        a = float(st.number_input("a:", value=1.0))
    with col2:
        b = float(st.number_input("b:", value=1.0))
    with col3:
        c = float(st.number_input("c:", value=1.0))

    if a != 0:
        st.markdown("Usted ingresó la siguiente ecuación:")
        st.latex(f"{a}x^2 + {b}x + {c} = 0")
    else:
        st.error("El coeficiente a debe ser diferente de cero.")

st.subheader("Discriminante")
st.markdown('''
El **discriminante** de una ecuación cuadrática está dado por la expresión:
$$
\\Delta = b^2 - 4ac.
$$

Analizar el discriminante me permite la siguiente interpretación:
- Si $\\Delta > 0$, la ecuación tiene dos soluciones reales.
- Si $\\Delta = 0$, la ecuación tiene una única solución real.
- Si $\\Delta < 0$, la ecuación no tiene soluciones reales.
''')

disc = b**2 - 4*a*c

with st.container(border=True):
    st.markdown('''
    El discriminante que se obtiene de la ecuación que usted ingresó es:
    ''')
    st.latex(f"\\Delta = ({b})^2 - 4({a})({c}) = {disc}")
    if disc > 0:
        st.markdown("> **Conclusión:** La ecuación tiene dos soluciones reales.")
    elif disc == 0:
        st.markdown("> **Conclusión:** La ecuación tiene una única solución real.")
    else:
        st.markdown("> **Conclusión:** La ecuación no tiene soluciones reales.")

st.subheader("Solucionar ecuaciones cuadráticas")
st.markdown('''
La solución de una ecuación cuadrática está dada por la fórmula:
$$
x = \\frac{-b \\pm \\sqrt{\\Delta}}{2a}.
$$

> A partir del análisis del discriminante, se puede concluir que la ecuacion tiene soluciones reales cuando el discriminante $\\Delta$ es no negativo.
''')

with st.container(border=True):
    st.markdown("**Solución de la ecuación ingresada:**")

    if disc > 0:
        x1 = (-b + disc**0.5)/(2*a)
        x2 = (-b - disc**0.5)/(2*a)

        st.latex(f"x_1 = \\frac{{-({b}) + \\sqrt{{{disc}}}}}{{2({a})}} = {x1:.4f}")
        st.latex(f"x_2 = \\frac{{-({b}) - \\sqrt{{{disc}}}}}{{2({a})}} = {x2:.4f}")
    elif disc == 0:
        x1 = -b/(2*a)

        st.latex(f"x = \\frac{{-({b})}}{{2({a})}} = {x1:.4f}")
    else:
        st.markdown("La ecuación no tiene soluciones reales.")

st.subheader("Interpretación geométrica.")
st.markdown('''
Las soluciones de una ecuación cuadrática corresponden con las raices (también llamados interceptos con el eje x) que define la función cuadrática $f(x) = ax^2+bx+c$.
''')

with st.container(border=True):
    st.markdown("**Gráfica de la función cuadrática:**")
    
    col1, col2 = st.columns([1, 2], gap="medium")

    with col1:
        ini = float(st.number_input("Inicio:", value=-5.0))
        fin = float(st.number_input("Final:", value=5.0))
        if disc < 0:
            st.markdown("> Observe que la función no tiene ningun intercepto con el eje x. Por eso, no tiene soluciones reales.")
        elif disc == 0:
            st.markdown("> Observe que cuando tiene una única solución real, el intercepto corresponde con el vértice de la parábola.")
    
    with col2:
        x = np.linspace(ini, fin, 100)
        y = a*x**2 + b*x + c
        
        fig, ax = plt.subplots()        # crear un canvas vacio
        ax.plot(x, y)                   # crear la curva
        ax.plot([ini, fin], [0,0])      # grafica el eje x
        if disc > 0:
            ax.scatter([x1, x2], [0, 0])    
        elif disc == 0:
            ax.scatter([x1], [0])

        st.pyplot(fig)
