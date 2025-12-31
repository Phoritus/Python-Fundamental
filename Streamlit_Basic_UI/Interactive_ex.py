import streamlit as st

st.title('Interactive Widget Example')

# CheckBox
if st.checkbox('Show/Hide'):
    st.write('Checkbox is checked')


# Select Box
option = st.selectbox('Category', ['Toy','Food','Entertainment','Shopping'])
st.write(f'You selected: {option}')


# Multiselect
options = st.multiselect('Select multiple numbers',[1,2,3,4,5])
st.write(f'You selected: {options}')