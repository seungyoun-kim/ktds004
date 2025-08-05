import streamlit as st

x = st.slider("Select a value", 0, 100, 50)
st.write(f"You selected: {x}")