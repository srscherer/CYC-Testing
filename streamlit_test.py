# streamlit_test
# https://srscherer-cyc-testing-streamlit-test-3stp49.streamlit.app/

import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.title("CYC Internal Analytics Dashboard")

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30 , 40]
})

st.header("Testing Datasets")
st.subheader("Dataframes")
st.write("We can display a dataframe that can be manipulated and viewed in the dashboard:")
st.write(df)

st.header("Testing Visualization Methods")
st.subheader("Line Chart")
st.write("Here's an example of plotting a time chart for filler data:")

chart_data = pd.DataFrame(
     [50.6, 43.5, 34.7, 30.2, 28.4, 20, 23, 18],
     columns=['Acceptance Rate'])

st.line_chart(chart_data)


st.write("We can also visualize percentage demographics with an interactive pie chart:")
demographic_data = pd.DataFrame({
    'count': [20, 6, 15, 3],
    'ethnicity': ['White', 'Black', 'Asian', 'Hispanic']
})

st.subheader("Pie Chart")
pieChart = px.pie(demographic_data, values = 'count', names = 'ethnicity', title = 'Application Demographics 202X')
st.plotly_chart(pieChart)