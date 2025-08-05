import streamlit as st
import numpy as np
import pandas as pd


print("This is a test script for Streamlit.")

char_data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=["a", "b", "c"]
)

st.line_chart(char_data)