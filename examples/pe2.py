# librerias
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
plt.style.use("ggplot")

# funciones
def formato(num):
    if num%1 == 0:
        return int(num)
    else:
        return num

# programa
st.title("Sistemas de ecuaciones lineales de 2x2")

# P1: definir
st.markdown('''
Un **sistema de ecuaciones lineales** de segundo grado, se podría definir como un sistema de ecuaciones lineales de la forma

$$
ax + by = e
$$

$$
cx + dy = f,
$$

donde $a,b,c,d,e,f \\in \\mathbb{R}$ son constantes reales, y $x,y \\in \\mathbb{R}$ son variables o incognitas.
''')

with st.container(border=True):
    st.markdown("**Digite los coeficientes de su problema:**")

    col1, col2, col3 = st.columns(3, gap="medium")

    with col1:
        a = float(st.number_input("a:", value=1.0))
        c = float(st.number_input("c:", value=1.0))
    
    with col2:
        b = float(st.number_input("b:", value=1.0))
        d = float(st.number_input("d:", value=3.0))
    
    with col3:
        e = float(st.number_input("e:", value=1.0))
        f = float(st.number_input("f:", value=5.0))
    
    st.markdown("La ecuación ingresada fue: ")
    st.latex(f"{formato(a)}x {'+' if b>=0 else ''} {formato(b)}y = {formato(e)}")
    st.latex(f"{formato(c)}x {'+' if d>=0 else ''} {formato(d)}y = {formato(f)}")

# part 2:
st.subheader("Análisis del determinante:")
st.markdown('''
El **determinante** de un sistema 2x2 está definido por la expresión:
$$
\\Delta = \\left| \\begin{matrix} a & b \\\\ c & d \\end{matrix} \\right| = ad - bc.
$$

Analizar el determinante permite saber si un sistema lineal tiene solución única.
- Si $\\Delta \\neq 0$, significa que el sistema tiene solución única.
- Si $\\Delta = 0$, significa que el sistema tiene infinitas soluciones o no tiene solución.
''')

det = a*d - b*c

with st.container(border=True):
    st.markdown(f'''
    El determinante calculado para el sistema que se ingresó fue:

    $$
    \\Delta = \\left| \\begin{{matrix}} {a} & {b} \\\\ {c} & {d} \\end{{matrix}} \\right| = ({a})({d}) - ({b})({c}) = {det}
    $$
    ''')

    if det != 0:
        st.markdown("> El sistema tiene solución única.")
    elif (c!=0 and f!=0 and (a/c) == (e/f)) or (d!=0 and b!=0 and (c/d) == (f/b)):
        st.markdown("> El sistema tiene infinitas soluciones.")
    else:
        st.markdown("> El sistema no tiene solución.")

# part 3
st.subheader("Solución del sistema")
st.markdown('''
La solución de un sistema de ecuaciones lineales puede obtenerse por diferentes métodos. Uno de los más usados es la regla de Cramer que propone que la solución del sistema (si existe), está dada por la expresión:

$$
x = \\frac{\Delta_x}{\Delta} = \\frac{ed - bf}{ad - bc}
$$

$$
y = \\frac{\Delta_y}{\Delta} = \\frac{af - ec}{ad - bc}
$$

> **Nota:** observe que la expresión del denominador corresponde con el determinante del sistema. Por eso, cuando $\Delta = 0$, el sistema no tiene única solución.
''')

with st.container(border=True):
    if det == 0:
        st.error("El sistema no tiene solución única porque $\Delta = 0$. Si quiere visualizar una solución, por favor digite un sistema con solución única.")
    else:
        x0 = (e*d - b*f)/det
        y0 = (a*f - e*c)/det

        st.markdown(f'''
        La solución del sistema ingresado es:

        $$
        x = \\frac{{({e})({d}) - ({b})({f})}}{{{det}}} = {x0:.4f}
        $$

        $$
        y = \\frac{{({a})({f}) - ({e})({c})}}{{{det}}} = {y0:.4f}
        $$
        ''')

# part 4
st.subheader("Interpretación geometríca")
st.markdown('''
Geométricamente, uno puede considerar cada ecuación del sistema lineal como la definición de una recta en el plano. De este modo, la solución del sistema corresponde con el punto en el que las rectas se intersectan.

Observe que:
* El sistema tiene solución única, si las rectas se intersectan en un solo punto.
* El sistema tiene infinitas soluciones, si las rectas son la misma.
* El sistema no tiene solución, si las rectas son paralelas y nunca se intersectan.
''')

with st.container(border=True):
    col1, col2 = st.columns([3, 1], gap="medium")    

    with col1:
        if det != 0:
            ini = x0 - 5
            fin = x0 + 5
        else:
            ini = -5
            fin = 5
        
        x = np.linspace(ini, fin, 4)
        r1 = (e - a*x)/b
        r2 = (f - c*x)/d

        fig, ax = plt.subplots()
        ax.plot(x, r1, label=f"${formato(a)}x {'+' if b>=0 else ''} {formato(b)}y = {formato(e)}$", c="turquoise")
        ax.plot(x, r2, label=f"${formato(c)}x {'+' if d>=0 else ''} {formato(d)}y = {formato(f)}$", c="mediumslateblue", ls="--")
        if det != 0:
            ax.scatter(x0, y0, c="orange")
            ax.annotate(f"({x0:.2f}, {y0:.2f})", [x0, y0], [x0, y0+1.2])

        ax.legend()
        st.pyplot(fig)
        
    with col2:
        if det != 0:
            st.markdown('''
            > Observe que el sistema tiene solución única y el punto solución encontrado corresponde con el punto donde se intersectan las rectas.
            ''')
        
        elif (c!=0 and f!=0 and (a/c) == (e/f)) or (d!=0 and b!=0 and (c/d) == (f/b)):
            st.markdown('''
            > Observe que el sistema tiene infinitas soluciones porque las dos rectas ingresadas corresponden a la misma recta.
            ''')
        
        else:
            st.markdown('''
            > Observe que el sistema no tiene solución porque las dos rectas ingresadas son paralelas.
            ''')
