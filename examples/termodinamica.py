import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

def f(n, x):
    return n/x

def g(n, x):
    return (n/x)**(5/7)


st.title("Aplicaciones del cambio de variables en integrales múltiples para la Ingeniería")

st.markdown('''
En determinados problemas de termodinámica, el trabajo se podría definir como el área de una determinada región $R$ acotada por las respectivas gráficas de los procesos termodinámicos.
Para la resolución del problema es necesario graficar la región $R$ delimitada por las funciones:
''')

st.latex(r'''
\left\{
    \begin{array}{ll}
        xy = a \\
        xy = b \\
        xy^{1.4} = c \\
        xy^{1.4} = d
\end{array}
\right.

''')

with st.container(border=True):
    st.subheader("Digite los parámetros del problema:")
    col1, col2 = st.columns([3, 7], gap="medium")

    with col1:
        a = st.number_input("a:", min_value=0.01, value=0.9)
        b = st.number_input("b:", min_value=0.01, value=1.2)
        c = st.number_input("c:", min_value=0.01, value=1.)
        d = st.number_input("d:", min_value=0.01, value=1.5)
    with col2:
        n1, n2 = (float(a)**3.5)/(float(c)**2.5), (float(a)**3.5)/(float(d)**2.5)
        n3, n4 = (float(b)**3.5)/(float(c)**2.5), (float(b)**3.5)/(float(d)**2.5)

        x1 = np.linspace(n2, n1, 100)
        x2 = np.linspace(n4, n3, 100)
        x3 = np.linspace(n1, n3, 100)
        x4 = np.linspace(n2, n4, 100)

        fig, ax = plt.subplots()
        ax.plot(x1, f(a,x1), label=f"$xy={a}$")
        ax.plot(x2, f(b,x2), label=f"$xy={b}$")
        ax.plot(x3, g(c,x3), label=f"$xy^{{1.4}}={c}$")
        ax.plot(x4, g(d,x4), label=f"$xy^{{1.4}}={d}$")

        ax.set_title("Region $R$")
        ax.set_xlabel("Volumen")
        ax.set_ylabel("Presión")
        ax.legend()

        st.pyplot(fig)

st.markdown(r'''
Aunque el problema se podría abordar al dividir la región $R$ en tres sub-regiones e integral cada región por aparte, la geometría de la región permite que al realizar un cambio de variable para que resulte posible integrar la región en una sola integral más simple.

La transformación aplicada para facilitar el proceso de la integral podría ser:
$$
T: \mathbb{R}^{2}\rightarrow\mathbb{R}^{2} 
$$

$$
T\begin{pmatrix} u \\ v \end{pmatrix} = \begin{pmatrix} xy \\ xy^{1.4} \end{pmatrix}
$$

Es decir, se aplica la sustitución $u=xy$ y $v=xy^{1.4}$. Entonces, se puede establecer que la región $D$ en el plano $uv$ la cuál es equivalente a la región $R$ en el plano $xy$ se podría definir matemáticamente como:
$$
D = \Big\{\begin{pmatrix} u \\ v \end{pmatrix} \in \Pi_{uv} \phantom{a}\big\|\phantom{a} (a \leq u \leq b) \wedge (c \leq v \leq d) \phantom{a}\Big\}
$$
''')

with st.container(border=True):
    col1, col2 = st.columns([3, 7], gap="medium")

    with col1:
        st.markdown(f'''
        En este caso, la región $D$ está definida por el cuadrilátero delimitado por las rectas:
        $$
        \\left[
            \\begin{{array}}{{ll}}
                u = {a} \\\\
                u = {b}
        \end{{array}}
        \\right.
        $$
        y 
        $$
        \\left[
            \\begin{{array}}{{ll}}
                v = {c} \\\\
                v = {d}
        \end{{array}}
        \\right.
        $$
        ''')

    with col2:
        fig, ax = plt.subplots()
        ax.plot([a,a], [c,d], label=f"$xy={a}$")
        ax.plot([b,b], [c,d], label=f"$xy={b}$")
        ax.plot([a,b], [c,c], label=f"$xy^{{1.4}}={c}$")
        ax.plot([a,b], [d,d], label=f"$xy^{{1.4}}={d}$")

        ax.set_xlim(a-0.2, b+0.2)
        ax.set_ylim(c-0.2, d+0.2)
        ax.set_ylabel('$v$')
        ax.set_xlabel('$u$')
        ax.set_title('Región $D$')
        ax.legend()

        st.pyplot(fig)


st.markdown(r'''
Para poder realizar el cambio de variable es necesario calcular el jacobiano de la transformación. Para calcular este, primero se calculará el jacobiano de la transformación inversa $T^{-1}$, el cual estaría definido por:
$$
\dfrac{\partial (u,v)}{\partial (x,y)} = \begin{vmatrix} \frac{\partial u}{\partial x} & \frac{\partial u}{\partial y} 
\\ \frac{\partial v}{\partial x} & \frac{\partial v}{\partial y} \end{vmatrix}
= \begin{vmatrix} y & x \\ y^{1.4} & 1.4xy^{0.4} \end{vmatrix} = 1.4xy^{1.4} - xy^{1.4} = 0.4xy^{1.4} 
$$

Dado que $v=xy^{1.4}$, se podría concluir que el jacobiano de la transformación está dado por:

$$
\dfrac{\partial (x,y)}{\partial (u,v)} = \frac{1}{\dfrac{\partial (u,v)}{\partial (x,y)}} = \dfrac{1}{0.4xy^{1.4}} = \dfrac{1}{0.4v} = \dfrac{5}{2v}
$$

Por tanto,
$$
W = \displaystyle\iint\limits_{R} dA = \iint\limits_{D} \frac{5}{2v} dA 
$$ 

$$ 
= {5\over2}\int\limits_{a}^{b}\int\limits_{c}^{d}\dfrac{1}{v}dv du 
$$

$$
= {5\over2}\int\limits_{b}^{a}\big[\ln(v)\big]_{c}^{d} du 
$$

$$
=  {5\over2}\int\limits_{b}^{a} \ln\Big({d \over c}\Big) du 
$$

$$
= {5\over2}\ln\Big({d \over c}\Big)\cdot\big[ u \big]_{a}^{b} 
$$

$$
W = \displaystyle{5\over2}(b-a)\cdot \ln\Big({d \over c}\Big) 
$$
''')

with st.container(border=True):
    W = 2.5*(b-a)*np.log(d/c)
    st.markdown(f'''
    Para los parámetros ingresados:
    $$
    W = \displaystyle{{5\\over2}}({b}-{a})\\cdot \\ln\\Big({{{d} \\over {c}}}\\Big) = {W:.4f}
    $$
    ''')