
# https://streamlit.io/
# pip install streamlit
# streamlit hello

import streamlit as st
import pandas as pd
 
st.write("""
        # My first app
        Hello *world!*
        """)
 
df = pd.read_csv("my_data.csv")
st.line_chart(df)

# number = st.slider("Pick a number", 0, 100)
# st.altair_chart(my_chart)
# file = st.file_uploader("Pick a file")
# color = st.color_picker("Pick color")
# pet = st.radio("Pick a pet", pets)