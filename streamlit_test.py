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



demographic_data = pd.DataFrame({
    'count': [20, 6, 15, 3],
    'ethnicity': ['White', 'Black', 'Asian', 'Hispanic']
})

st.subheader("Pie Chart")
st.write("We can also visualize percentage demographics with an interactive pie chart:")
pieChart = px.pie(demographic_data, values = 'count', names = 'ethnicity', title = 'Application Demographics 202X')
st.plotly_chart(pieChart)


st.subheader("Scatter Plot")
st.write("A scatter plot can be used to show correlation between two metrics:")
gpa_data = pd.DataFrame({
    'gpa': [3.4, 2, 4.0, 2.4, 3.9, 3.2, 1.9],
    'recommend': [3, 1, 4, 2, 4, 3, 0]
})
gpaCorrelation = px.scatter(gpa_data, x = 'gpa', y = 'recommend', title = 'GPA as a Predictor of Recommendation')
gpaCorrelation.update_traces(marker_size=10)
st.plotly_chart(gpaCorrelation)

st.subheader("Bar Chart")
st.write("A bar chart can be used to show numbers of items in different categories:")
year_data = pd.DataFrame({
    'applications received': [20,34, 40, 67],
    'year': ['2019', '2020', '2021', '2022']
})
barChart = px.bar(year_data, x='year', y='applications received')
st.plotly_chart(barChart)


st.write("This data could also be displayed in a plotly line chart to show chronological progression:")
timeChart = px.line(year_data, x='year', y='applications received', title = 'Number of Applications Received Over Time')
st.plotly_chart(timeChart)


st.subheader("Pulling data from a Google Sheets")
def load_data(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)
df = load_data("https://docs.google.com/spreadsheets/d/1hRBqJrxF99JjLNzA1w4go0-hDp4jVofAb0SoddPTLis/edit?usp=sharing")
# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")