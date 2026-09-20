import streamlit as st
st.title("Price Calculator",text_alignment='center')
product_price = st.number_input("Enter the price of product: ")
discount_percent = st.slider("Select discount percentage",0,50)
if st.button("Calculate Final Price!"):
    final_price = product_price - (product_price*(discount_percent/100))
    st.success(f"The price of the product after discount is: {final_price}")