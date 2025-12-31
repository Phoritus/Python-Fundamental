import streamlit as st

st.title('Expense Management System')

date = st.date_input('Expense Date:')
if date:
    st.text(f'In Date: {date}')