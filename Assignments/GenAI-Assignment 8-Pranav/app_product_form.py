import streamlit as st
product_name = st.sidebar.text_input("Product Name: ")
category = st.sidebar.selectbox("Select Product Category:",['Utilities','Home Care','Snacks and Beverages'])
price = st.sidebar.number_input("Enter price of the product:")
if st.sidebar.button("Add Product"):
    st.success(f"""The following product has been successfully added:
                    Product Name:{product_name}
                    Product Category: {category}
                    Product Price: {price}""")