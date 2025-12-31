import streamlit as st
import pandas as pd


# Text elements
st.title('Streamlit Core Features')
st.subheader('Text Elements')
st.text('This is a simple text element')

data = {
    'Category': ['Entertainment','Shopping','Food','Other'],
    'Total': [150,570,585,75]
}

df = pd.DataFrame(data)
df = df.reset_index(drop=True)

# Data display
st.subheader('Fetch with sum category')
st.write('Start Date: 2024-08-02 | End Date:2024-08-04')
st.dataframe(df)


# Charts
st.subheader('Charts')
st.line_chart([150,570,585,75,5])

# User Input
st.subheader("User Input")
value = st.slider('Select a value',0, 100)
st.write(f'Selected value: {value}')