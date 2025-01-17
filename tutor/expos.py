import streamlit as st
import pandas as pd

st.title("Proyectos finales 2024-I")

st.header("Grupo :blue[PE1]", divider="blue")

pe1 = pd.read_csv("static/pe1.csv")
pe1["Código"] = pe1["Código"].astype("string")
pe1 = pe1.sample(frac=1, random_state=1107)

st.dataframe(pe1, hide_index=True, use_container_width=True, column_config={"Código":st.column_config.TextColumn(), "Link":st.column_config.LinkColumn()})

st.header("Grupo :orange[PE2]", divider="orange")

pe2 = pd.read_csv("static/pe2.csv")
pe2["Código"] = pe2["Código"].astype("string")
pe2 = pe2.sample(frac=1, random_state=1107)

st.dataframe(pe2, hide_index=True, use_container_width=True, column_config={"Código":st.column_config.TextColumn(), "Link":st.column_config.LinkColumn()})