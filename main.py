import streamlit as st

pg = st.navigation({
    "Resumen":[
        st.Page("tutor/comandos.py", title="Comandos", icon=":material/code:"),
        st.Page("tutor/preguntas.py", title="Preguntas", icon=":material/question_mark:"),
        st.Page("tutor/expos.py", title="Exposiciones", icon=":material/co_present:"),
    ],
    "Ejemplos":[
        st.Page("examples/juego.py", title="Adivinador", icon="🔮"),
        st.Page("examples/termodinamica.py", title="Máquina de carnot", icon="🔌"),
        st.Page("examples/pe1.py", title="PE1: ecuación cuadrática", icon="1️⃣"),
        st.Page("examples/pe2.py", title="PE2: sistemas lineales", icon="2️⃣"),
    ]
})

pg.run()
