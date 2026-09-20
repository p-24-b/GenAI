import streamlit as st
st.title('Simple Sales Dashboard')
st.text("This dashboard displays the monthly sales of the month selected")
month = st.selectbox("Select the month",['January','February','March','April'])
sales ={'January':1200,'February':1500,'March':900,'April':2000}
st.write(f"The sales for {month} is: {sales[month]}")
st.bar_chart(list(sales.values()))
