import streamlit as st
st.title("Streamlit Webpage")
st.header("Hello Everyone")
st.text("This is my first webpage built on streamlit")
if st.button("Click Me"):
    st.write("The button has been clicked")
level = st.slider("Select a level",1,10,0,2)
st.write(f'Selected Level:{level}')

