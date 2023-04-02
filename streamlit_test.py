# streamlit_test
# https://srscherer-cyc-testing-streamlit-test-3stp49.streamlit.app/

import streamlit as st
import numpy as np
import pandas as pd

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30 , 40]
})

st.write("Here's our first attempt at using data to create a table:")
st.write(df)

st.write("Heres an example of plotting a time chart for filler data:")

chart_data = pd.DataFrame(
     [50.6, 43.5, 34.7, 30.2, 28.4, 20, 23, 18],
     columns=['Acceptance Rate'])

st.line_chart(chart_data)