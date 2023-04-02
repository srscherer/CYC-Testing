# streamlit_test

import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30 , 40]
})

st.write("Here's our first attempt at using data to create a table:")
st.write(df)

st.write("Heres an example of plotting a time chart for filler data:")

timeChart = pd.DataFrame({
    'Application Cycle': ["Fall 2020", "Spring 2021", "Fall 2021", "Spring 2022", "Fall 2022", "Spring 2023"],
    'Acceptance Rate': [50.5, 45.6, 33.4, 39, 21, 18]
})

st.line_chart(timeChart)