import streamlit as st
import pandas

data = {
  'series_1':[1, 2, 3, 4, 5, 7],
  'series_2':[10, 30, 40, 100, 250]
}

df = pandas.DataFrame(data)

st.title('Our First Streamlit App')
st.subheader('Interduce Streamlit Python app')
st.write('''This is our first websiteApp.
Enjoy it More
''')
st.write(df)
